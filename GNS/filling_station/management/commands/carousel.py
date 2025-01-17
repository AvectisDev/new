import serial
import struct
import logging
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='carousel.log',
    filemode='w',
    encoding='utf-8'
)

logger = logging.getLogger('carousel')
logger.setLevel(logging.DEBUG)

# Функция для вычисления CRC-16/AUG-CCITT
def calc_crc(message):
    poly = 0x1021
    reg = 0xFFFF
    message += b'\x00\x00'
    for byte in message:
        mask = 0x80
        while (mask > 0):
            reg <<= 1
            if byte & mask:
                reg += 1
            mask >>= 1
            if reg > 0xffff:
                reg &= 0xffff
                reg ^= poly
    return reg


# Указываем порт и скорость соединения
port = 'COM3'
baud_rate = 9600

ser = None

try:
    # Создаем объект Serial для работы с COM-портом
    ser = serial.Serial(port, baud_rate, timeout=1)
    logger.debug(f"Соединение установлено на порту {port}.")

    while True:
        # Читаем данные из COM-порта
        data = ser.read(8)
        if data:
            # Выводим запрос в HEX формате
            print(f"Получен запрос: {data.hex().upper()} - {datetime.now()}")
            logger.debug(f"Получен запрос: {data.hex().upper()}")

            # Расшифровываем запрос
            request_type = data[0]
            post_number = data[1]
            measurement_number = data[2]
            # Измененная строка для вывода массы баллона
            # Преобразуем четвертый и пятый байты в десятичное значение массы баллона
            # weight_bytes = data[3:5]
            # Преобразуем четвертый и пятый байты в десятичное значение массы баллона
            weight_combined = (data[3] << 8) | data[4]
            service_byte = data[5]
            crc = int.from_bytes(data[6:8], byteorder='big')

            logger.debug(f"Тип запроса: {hex(request_type)}")
            logger.debug(f"Номер поста: {(post_number)}")
            logger.debug(f"Номер измерения: {hex(measurement_number)}")
            logger.debug(f"Масса баллона: {weight_combined} г")
            logger.debug(f"Флаг: {hex(service_byte)}")
            logger.debug(f"CRC: {hex(crc)}")

            # Формируем ответ
            if request_type == 0x7A:
                response_type = 0x5A
            elif request_type == 0x70:
                response_type = 0x50

            # Формируем ответный пакет без CRC
            response_data = struct.pack('<BBBHBH', response_type, post_number, 0xFF, 0x10A4, 0xFF, 0xFFFF)

            # Вычисляем CRC-16/AUG-CCITT для ответа (без последних двух байт)
            crc_t = calc_crc(response_data[:-2])
            crc = ((crc_t & 0xFF) << 8) | ((crc_t >> 8) & 0xFF)

            # Добавляем CRC к ответу
            response_with_crc = response_data[:-2] + struct.pack('<H', crc)

            # Отправляем ответ через COM-порт
            ser.write(response_with_crc)
            print(f"Отправлен ответ: {response_with_crc.hex().upper()} - {datetime.now()}")
            logger.debug(f"Отправлен ответ: {response_with_crc.hex().upper()}")

except serial.SerialException as e:
    print(f"Ошибка: {e}. Проверьте правильность указанного порта.")
    logger.error(f"Ошибка: {e}. Проверьте правильность указанного порта.")
finally:
    if ser:
        # Закрываем соединение только если оно было открыто
        ser.close()
        logger.debug("Соединение закрыто")
