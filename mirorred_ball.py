import sys

from PySide2.QtWidgets import (
	QMainWindow,
	QApplication,
	QLabel,
	QWidget,
	QVBoxLayout
	)
from PySide2.QtCore import QSize, QPoint


class MainWindow(QMainWindow):
	""" playing a little bit with properties """
	def __init__(self):
		super().__init__()
		self.setGeometry(500, 500, 400, 200) 

		self.setMouseTracking(True)

		self.circle = QLabel("o")
		self.circle.setFixedSize(QSize(20,20))
		
		self.setCentralWidget(self.circle)

	def mouseMoveEvent(self, e):
		pos = e.pos()
		x = 400-pos.x()
		y = 200-pos.y()
		self.circle.move(QPoint(x,y))

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec_()


