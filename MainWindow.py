from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QLabel

import requests
from PIL import Image
from io import BytesIO
import random

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QGridLayout()
window.setLayout(layout)
adress = QLineEdit()
adress2 = QLineEdit()


def Downloader():
    getAdress = requests.get(adress.text())
    image = Image.open(BytesIO(getAdress.content))
    picNum = random.randint(20,900)
    image.save('C:/Users/Zekaryas/Desktop/savefile/landscape%d.png'%(picNum), 'PNG')
directDownload = QLabel("directly download from an image url")
layout.setSpacing(10)
submitButton = QPushButton("Download")
submitButton2 = QPushButton("Download")
layout.addWidget(directDownload)

layout.addWidget(adress,0,1)
layout.addWidget(submitButton,0,2)
#facebook
directDownload = QLabel("directly download from facebook")
layout.setSpacing(10)
submitButton = QPushButton("Download")

layout.addWidget(directDownload,2,0)

layout.addWidget(adress2,2,1)
layout.addWidget(submitButton2,2,2)

submitButton.clicked.connect(Downloader)
window.show()
app.exec_()



    #getAdress = requests.get(screen.__get_adress.text())
    #image = Image.open(BytesIO(getAdress.content))
    #image.save('C:/Users/Zekaryas/Desktop/savefile/landscape.jpg', 'JPEG')
