import socket
import psycopg2
import datetime
import binascii
import time
from RFID_parameter import readers, COMMANDS


def write_nfc_tag(nfc_tag:str, status:str):
    """функция записывает в базу данных номер метки и дату проведения операции считывания"""

    try:
        conn =  psycopg2.connect(dbname="PinskGNS", host="localhost", user="postgres", password=".avectis1", port="5432")
        print("Connection with data base established")
        conn.autocommit = True

        with conn.cursor() as cursor:
            data = (nfc_tag, status, datetime.datetime.now())
            cursor.execute("INSERT INTO filling_station_ballon (nfc_tag, state, creation_date) VALUES (%s, %s, %s)", data)
            print("Data added")

        conn.close()
    
    except:
        print('Can`t establish connection to database')


def read_nfc_tag(reader:dict, command:str):
    """функция отправляет запрос на считыватель FEIG и получает в ответ дату, время и номер RFID метки """

    previous_nfc_tag = reader['nfc_tag']    # присваиваем предыдущую метку временной переменной

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.settimeout(1)
            print(f"Connecting to {reader['ip']}:{reader['port']}")
            s.connect((reader['ip'], reader['port']))  

            #send data to FEIG
            s.sendall(binascii.unhexlify(command))
            print('send complete')

            data = s.recv(2048)
            data_bytes = binascii.hexlify(data)
            buffer = data_bytes.decode()
            print('Recive complete. Data from reader: ', buffer)

            if len(buffer) > 18:
                nfc_tag = buffer[18:34]  # из буфера получаем новую метку
                if nfc_tag != previous_nfc_tag:
                    write_nfc_tag(nfc_tag, reader['status'])
                    print(nfc_tag)
            else:
                nfc_tag = previous_nfc_tag
           
            return nfc_tag  #из функции возвращаем значение считанной метки
        except:
            print(f'Can`t establish connection with RFID reader {reader['ip']}:{reader['port']}')     


# Program
while True:
    for reader in readers:
        reader['nfc_tag'] = read_nfc_tag(reader, COMMANDS['host_read'])
        time.sleep(1)
