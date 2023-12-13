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
        self.font.setPointSize(20)
        self.matrix = [
            ['ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
            ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
            ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'],
            ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Ctrl']
        ]
        self.generate_keyboard()

    def generate_keyboard(self):
        for i, row in enumerate(self.matrix):
            layout = QHBoxLayout()
            for word in row:
                btn = QPushButton(self)
                btn.setFont(self.font)
                btn.size()
                if i == 4:
                    if word == "Space":
                        w, h = 330, 60
                    else:
                        w, h = 90, 60
                        btn.setText(word)
                    btn.setMaximumSize(w, h)
                    btn.setMinimumSize(w, h)
                else:
                    if word in anbur:
                        btn.setText(anbur[word])
                    else:
                        btn.setText(word)
                    btn.setMaximumSize(60, 60)
                    btn.setMinimumSize(60, 60)
                btn.setStyleSheet(
                    """
                    QPushButton {
                        border-radius: 2px;
                        border: 1px solid;
                        box-shadow: 5px 5px 5px black;
                    }
                    QPushButton:hover {
                        background-color: #dbd0b0;
                        border: 2px solid;
                    }
                    
                    """
                )
                btn.clicked.connect(self.clicked_on_btn)
                size_policy = btn.sizePolicy()
                size_policy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(size_policy)
                layout.addWidget(btn)
            self.keyboard_layout.addLayout(layout)

    def clicked_on_btn(self):
        btn = self.sender()
        print(btn.text())
