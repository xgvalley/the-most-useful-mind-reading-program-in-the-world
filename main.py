import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QApplication)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setWindowTitle("世界上最有用的读心术程序")
		self.setGeometry(450, 250, 500, 500)

		self.promptLabel = QLabel("请输入你所想的文本～", self)
		self.promptLabel.setGeometry(0, 0, 500, 50)
		self.promptLabel.setFont(QFont("", 30))
		self.promptLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
		self.promptLabel.show()

		self.inputLineEdit = QLineEdit("", self)
		self.inputLineEdit.setGeometry(0, 60, 400, 30)
		self.inputLineEdit.setFont(QFont("", 30))
		self.inputLineEdit.show()

		self.okBtn = QPushButton("确认", self)
		self.okBtn.setGeometry(400, 60, 100, 30)
		self.okBtn.clicked.connect(self.ok)
		self.okBtn.show()

		self.resultLabel = QLabel("", self)
		self.resultLabel.setGeometry(0, 100, 500, 25)
		self.resultLabel.setFont(QFont("", 20))
		self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
		self.resultLabel.show()

		self.show()
	def ok(self):
		self.resultLabel.setText(f"您现在正在想：“{self.inputLineEdit.text()}”")


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
