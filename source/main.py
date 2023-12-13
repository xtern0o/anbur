import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    self = MainWindow()
    self.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
