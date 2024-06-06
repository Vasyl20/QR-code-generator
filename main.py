import qrcode

# URL для QR-коду
url = "https://ndekcrv.gov.ua/images/docs/2024/ZAYAVA_VIDSTRIL_2024.pdf"

# Генерація QR-коду
qr = qrcode.QRCode(
    version=1,  # Розмір QR-коду (1 - 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Рівень корекції помилок (L, M, Q, H)
    box_size=10,  # Розмір кожного квадратика QR-коду
    border=4,  # Ширина межі (кількість квадратів)
)

# Додаємо дані до QR-коду
qr.add_data(url)
qr.make(fit=True)

# Створення зображення QR-коду
img = qr.make_image(fill='black', back_color='white')

# Збереження зображення у файл
img.save("qr_code2.png")

print("QR-код згенеровано та збережено як qr_code.png")