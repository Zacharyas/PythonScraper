from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QLabel

import requests
from PIL import Image
from io import BytesIO
import random
import os
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QGridLayout()
window.setLayout(layout)
adress = QLineEdit()
adress2 = QLineEdit()
picNum = random.randint(20,900)

def Downloader():
    getAdress = requests.get(adress.text())
    image = Image.open(BytesIO(getAdress.content))
    image.save('C:/Users/yourusername/Desktop/Scraper/landscape%d.png'%(picNum), 'PNG')
    print("downloaded")

directDownload = QLabel("directly download from an image url")
layout.setSpacing(10)
submitButton = QPushButton("Download")
submitButton2 = QPushButton("Download2")
layout.addWidget(directDownload)

layout.addWidget(adress,0,1)
layout.addWidget(submitButton,0,2)
submitButton.clicked.connect(Downloader)
#facebook
directDownload = QLabel("directly download from facebook")
layout.setSpacing(10)
submitButton = QPushButton("Download")

layout.addWidget(directDownload,2,0)

layout.addWidget(adress2,2,1)
layout.addWidget(submitButton2,2,2)


window.show()
app.exec_()



    #getAdress = requests.get(screen.__get_adress.text())
    #image = Image.open(BytesIO(getAdress.content))
    #image.save('C:/Users/Zekaryas/Desktop/savefile/landscape.jpg', 'JPEG')
