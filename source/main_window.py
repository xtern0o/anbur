from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout

from anbur import anbur
from source.design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont('fonts/Everson Mono.ttf')
        self.font = QFont('Everson Mono')
        self.font.setPointSize(30)
        self.matrix = [['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
                       ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
                       ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']]

        self.generate_keyboard()

    def generate_keyboard(self):
        for row in self.matrix:
            layout = QHBoxLayout()
            for word in row:
                btn = QPushButton(self)
                btn.setFont(self.font)
                btn.size()
                btn.setText(anbur[word])
                size_policy = btn.sizePolicy()
                size_policy.setHorizontalStretch(1)
                size_policy.setVerticalStretch(1)
                size_policy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(size_policy)
                layout.addWidget(btn)
            self.keyboard_layout.addLayout(layout)
