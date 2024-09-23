# Instructions
'''
At first we install the virtual environment by this command:
    python -m venv venv
Then we activated the virtual environment by this command:
    venv \ Scripts \ activate
Then we install the QR code package using this command:
    pip install qrcode

----------------------

Just write the following command when you are done with the processing:
    deactivate

'''

import qrcode

def generateQRCode(data, fileName):
    qr = qrcode.QRCode(box_size=11, border=5)
    qr.add_data(data)

    image = qr.make_image(fill_color='black', back_color='white')
    image.save(fileName)

    print(f'QR code saved as {fileName}')


data = input('Enter the text or URL: ').strip()
fileName = input('Enter the filename: ').strip()

generateQRCode(data, fileName)


