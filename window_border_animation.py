import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, QPropertyAnimation, Property
from PySide2.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
	""" just a trick to create animation for border  """
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowFlags(Qt.FramelessWindowHint)

		self.setFixedSize(300,300)
		layout = QVBoxLayout()
		label = QLabel()
		label.setFixedSize(280,280)
		layout.addWidget(label, alignment=Qt.AlignCenter)
		self.setStyleSheet("QLabel{background-color:white}")
		self.blink_animation = QPropertyAnimation(self, b"backcolor")
		self.blink_animation.setStartValue(QColor(255,0,0))
		self.blink_animation.setKeyValueAt(0.5, QColor(0,0,255))
		self.blink_animation.setEndValue(QColor(255,0,0))
		self.blink_animation.setDuration(3000)

		#self.blink_animation.setLoopCount(-1)
		self.blink_animation.start()

		container = QWidget()
		container.setLayout(layout)
		self.setCentralWidget(container)

	def getBackColor(self):
		return self.palette().color(QPalette.Window)

	def setBackColor(self, color):
		pal = self.palette()
		pal.setColor(QPalette.Window, color)
		self.setPalette(pal)
	

	backcolor = Property(QColor, getBackColor, setBackColor)
if __name__ == "__main__":

	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()