import socket
import psycopg2
import datetime
import binascii
import time


def write_nfc_tag(nfcTag):
    """функция записывает в базу данных номер метки и дату проведения операции считывания
    в демо-режиме работает только 1 считыватель, поэтому всем баллонам будет присвоен статус 'Наполнение' """

    try:
        conn =  psycopg2.connect(dbname="PinskGNS", host="localhost", user="postgres", password=".avectis1", port="5432")
        print("Connection established")
        conn.autocommit = True

        with conn.cursor() as cursor:
            data = (nfcTag, "Наполнение", datetime.datetime.now())
            cursor.execute("INSERT INTO filling_station_ballon (nfc_tag, state, creation_date) VALUES (%s, %s, %s)", data)
            print("Данные добавлены")

        conn.close()
    
    except:
        print('Can`t establish connection to database')


nfc_tag = ''

HOSTS_LIST = {
    'reader_1': '10.10.2.20', 
    'reader_2': '10.10.2.21', 
    'reader_3': '10.10.2.22', 
    'reader_4': '10.10.2.23', 
    'reader_5': '10.10.2.24', 
    'reader_6': '10.10.2.25', 
    'reader_7': '10.10.2.26', 
    'reader_8': '10.10.2.27', 
    }
PORT = 10001            # The same port
COMMANDS = {
    '020009ffb001001843'
}

HOST = '10.10.2.26'     # The remote host for test


def rfid_reader(ip, port, command, tag):
    global nfc_tag
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            print("Connecting...")
            s.connect((ip, port))  

            #send data to FEIG
            s.sendall(binascii.unhexlify(command))
            print('send complete')
            data = s.recv(2048)
            data_bytes = binascii.hexlify(data)
            buffer = data_bytes.decode()
            print('Recive complete. Data from reader: ', buffer)

            if len(buffer) > 18:
                previous_nfc_tag = nfc_tag
                nfc_tag = buffer[18:34]
            if nfc_tag != previous_nfc_tag:
                write_nfc_tag(nfc_tag)
                print(nfc_tag)
        except:
            print('Can`t establish connection to RFID reader')     
        

while True:
    time.sleep(2)
    rfid_reader()


