import os
from os import system

try:
    import qrcode
except:
    os.system("pip install qrcode")
    os.system("pip install qrcode[pil]")

try:
    import datetime
    from datetime import datetime
except:
    os.system("pip install datetime")




try:
    time = datetime.today().strftime('%d.%m.%y %H:%M')
except:
    pass

url = input("укажите ссылку или же текст: ")
name = input("укажите названия файла(без формата): ")

try:
    with open('info/url.txt', 'w') as f:
        f.write(url)
except:
    print("ошибка")
    input()





qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"qr/{name}.jpg", "JPEG")