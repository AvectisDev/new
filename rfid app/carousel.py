import os
import serial
import struct
import logging
import balloon_api


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
# Создаём папку logs, если её нет
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=os.path.join(LOGS_DIR, 'carousel.log'),
    filemode='w',
    encoding='utf-8'
)

logger = logging.getLogger('carousel_logger')
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

def serial_exchange():
    try:
        logger.debug(f"Запуск программы обработки УНБ...")
        # Создаем объект Serial для работы с COM-портом
        ser = serial.Serial(port, baud_rate, timeout=1)
        logger.debug(f"Соединение установлено на порту {port}.")

        while True:
            # Читаем 8 байт данных из COM-порта
            data = ser.read(8)

            if data:
                # Расшифровываем каждый байт по отдельности
                request_type = data[0]
                post_number = data[1]
                measurement_number = data[2]
                # Преобразуем четвертый и пятый байты в десятичное значение массы баллона
                weight_combined = (data[3] << 8) | data[4]
                service_byte = int.from_bytes(data[5:7], byteorder='little')
                crc = int.from_bytes(data[6:8], byteorder='little')

                logger.debug(f"Получен запрос от поста. Тип запроса: {hex(request_type)}. Номер поста: {post_number} "
                             f"Масса баллона: {weight_combined}")

                # формируем запрос к серверу на обновление данных
                post_data = {
                    'request_type': str(hex(request_type)),
                    'post_number': post_number,
                    'weight_combined': weight_combined
                }
                response = balloon_api.put_carousel_data(post_data)
                logger.debug(f'Ответ от сервера {response}')

                if response.get('error'):
                    logger.error(f"Данные получены от сервера. Ошибка - {response}")
                elif response.get('full_weight'):
                    full_weight = response.get('full_weight')
                    if full_weight:
                        full_weight = int(full_weight * 1000)
                    logger.debug(f"Данные получены от сервера - {response}. "
                                 f"Записываем вес {full_weight} в пост")
                else:
                    logger.debug(f"Данные получены от сервера - {response}")

    except serial.SerialException as e:
        logger.error(f"Ошибка: {e}. Проверьте правильность указанного порта.")
    except Exception as error:
        logger.error(f"Общая ошибка: {error}.")
    finally:
        if ser:
            # Закрываем соединение только если оно было открыто
            ser.close()
            logger.debug("Соединение закрыто")


# if __name__ == "__main__":
while True:
    serial_exchange()
