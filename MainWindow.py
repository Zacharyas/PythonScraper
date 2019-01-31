from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QLabel

import requests
from PIL import Image
from io import BytesIO
import random
import os
import instaloader
picNum = random.randint(20,900)
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QGridLayout()
window.setLayout(layout)
adress = QLineEdit()
adress2 = QLineEdit()

#Method for downloading from a direct url
def directUrlDownloader():
    getAdress = requests.get(adress.text())
    image = Image.open(BytesIO(getAdress.content))
    image.save('C:/Users/yourusername/Desktop/Scraper/picture%d.png'%(picNum), 'PNG')
    print("downloaded")
#method for displaying direct url download field
def directUI():
    directDownload = QLabel("directly download from an image url")
    layout.setSpacing(10)
    submitButton = QPushButton("Download")
    layout.addWidget(submitButton)
    layout.addWidget(adress,0,1)
    layout.addWidget(submitButton,0,2)
    submitButton.clicked.connect(directUrlDownloader)


directUI()
window.show()
app.exec_()



    #getAdress = requests.get(screen.__get_adress.text())
    #image = Image.open(BytesIO(getAdress.content))
    #image.save('C:/Users/Zekaryas/Desktop/savefile/landscape.jpg', 'JPEG')
