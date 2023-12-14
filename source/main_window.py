from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout

from anbur import anbur
from config import CONFIG
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

        self.frame_2.setStyleSheet(
            f"""
            background-color: {CONFIG["keyboard"]["background-color"]}
            """
        )

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
                    f"""
                    QPushButton {{
                        border-radius: 2px;
                        background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                        color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};                        
                    }}
                    QPushButton:hover {{
                        background-color: {CONFIG["keyboard"]["key"]["background-color"]["hover"]};
                        color: {CONFIG["keyboard"]["key"]["text-color"]["hover"]};
                    }}
                    QPushButton:pressed {{
                        background-color: {CONFIG["keyboard"]["key"]["background-color"]["active"]};
                        color: {CONFIG["keyboard"]["key"]["text-color"]["active"]};
                    }}
                    """
                )
                btn.setFlat(True)
                btn.clicked.connect(self.clicked_on_btn)
                size_policy = btn.sizePolicy()
                size_policy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(size_policy)
                layout.addWidget(btn)
            self.keyboard_layout.addLayout(layout)

    def clicked_on_btn(self):
        btn = self.sender()
        print(btn.text())
