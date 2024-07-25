readers = [{} for i in range(12)]

# Считыватели на отгрузке
# 1-й дальний от цеха
readers[0] = {
    'ip': '192.168.100.61', 
    'port': 10001, 
    'status': 'Погрузка полного баллона на тралл 1 (RFID №1)',
    'nfc_tag': ''
    }

# 2-й ближе к цеху
readers[1] = {
    'ip': '192.168.100.62', 
    'port': 10001, 
    'status': 'Погрузка полного баллона на тралл 2 (RFID №2)',
    'nfc_tag': ''
    }

# Считыватели на приёмке
# 3-й дальний от цеха
readers[2] = {
    'ip': '192.168.100.63', 
    'port': 10001, 
    'status': 'Приёмка пустого баллона из тралла 1 (RFID №3)',
    'nfc_tag': ''
    }

# 4-й ближе к цеху
readers[3] = {
    'ip': '192.168.100.64', 
    'port': 10001, 
    'status': 'Приёмка пустого баллона из тралла 2 (RFID №4)',
    'nfc_tag': ''
    }

# Выход из наполнительного цеха
readers[4] = {
    'ip': '192.168.100.65', 
    'port': 10001, 
    'status': 'Регистрация полного баллона на складе (RFID №5)',
    'nfc_tag': ''
    }

# Вход в наполнительный цех
readers[5] = {
    'ip': '192.168.100.66', 
    'port': 10001, 
    'status': 'Регистрация пустого баллона в цеху (RFID №6)',
    'nfc_tag': ''
    }

# Считыватели в цеху
# Карусель №1
readers[6] = {
    'ip': '192.168.100.67', 
    'port': 10001, 
    'status': 'Наполнение баллона сжиженным газом. Карусель №1 (RFID №7)',
    'nfc_tag': ''
    }

# Карусель №2
readers[7] = {
    'ip': '192.168.100.68', 
    'port': 10001, 
    'status': 'Наполнение баллона сжиженным газом. Карусель №2 (RFID №8)',
    'nfc_tag': ''
    }

readers[8] = {
    'ip': '192.168.100.69', 
    'port': 10001, 
    'status': 'Вход в наполнительный цех из ремонтного (RFID №9)',
    'nfc_tag': ''
    }

readers[9] = {
    'ip': '192.168.100.70', 
    'port': 10001, 
    'status': 'Выход из наполнительного цеха в ремонтный (RFID №10)',
    'nfc_tag': ''
    }

readers[10] = {
    'ip': '192.168.100.71', 
    'port': 10001, 
    'status': 'Вход в ремонтный цех из наполнительного (RFID №11)',
    'nfc_tag': ''
    }

readers[11] = {
    'ip': '192.168.100.72', 
    'port': 10001, 
    'status': 'Выход из ремонтного цеха в наполнительный (RFID №12)',
    'nfc_tag': ''
    }

# Комманды, посылаемые на считыватель
COMMANDS = {
    'host_read': '020009ffb001001843',
    'read_complete': '02000DFF72010181010019236B', #зажигаем зелёную лампу на считывателе на 2.5 сек
    'read_complete_with_error': '',
    'buffer_read': '020009FFB02B005B9D', 
}