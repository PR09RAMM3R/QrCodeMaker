import qrcode
while True:
    path = input('QR Code manzilni kiriting: ')
    name = input('QR Code qanday nom bilan saqlansin: ')
    qrcode.make(path).save(name + '.png')