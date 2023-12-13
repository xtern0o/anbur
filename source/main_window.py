from PyQt5.QtWidgets import QMainWindow

from source.design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

    def generate_keyboard(self):

