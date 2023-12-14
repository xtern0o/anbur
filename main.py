import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from source.main_window import MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    self = MainWindow()
    self.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
