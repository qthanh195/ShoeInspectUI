from PySide6.QtWidgets import QApplication
from process import MySideBar
import sys

app = QApplication(sys.argv)

window = MySideBar()

window.show()
sys.exit(app.exec())