from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
adress = QLineEdit()
submitButton = QPushButton("Submit")
layout.addWidget(adress)
layout.addWidget(submitButton)

window.setLayout(layout)
window.show()
app.exec_()
