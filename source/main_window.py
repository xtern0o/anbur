from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFontDatabase, QFont, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QPlainTextEdit, QApplication

from .anbur import anbur
from source.config import CONFIG
from source.design import Ui_MainWindow

keyboard_btn = dict()


class MyPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super(MyPlainTextEdit, self).__init__(parent)

    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()

        if modifiers & Qt.ControlModifier:
            if event.key() == Qt.Key_A:
                self.selectAll()
                return
            elif event.key() == Qt.Key_C:
                self.copy()
                return
            elif event.key() == Qt.Key_V:
                self.paste()
                return
            elif event.key() == Qt.Key_X:
                self.cut()
                return

        if event.key() == Qt.Key_Backspace:
            super(MyPlainTextEdit, self).keyPressEvent(event)
        # print(keyboard_btn)
        key = QKeySequence(event.key()).toString().lower()
        keyboard_btn[key].animateClick()
        super(MyPlainTextEdit, self).keyPressEvent(event)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont('fonts/Everson Mono.ttf')
        self.font = QFont('Everson Mono')
        self.font.setPointSize(20)
        self.plain_text_edit_2.setFont(self.font)
        self.matrix = [
            ['ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
            ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
            ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
            ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'],
            ['Ctrl', 'Win', 'Alt', 'space', 'Alt', 'Ctrl']
        ]
        self.generate_keyboard()

        self.set_initial_stylesheets()

    def set_initial_stylesheets(self):
        self.frame_2.setStyleSheet(
            f"""
            background-color: {CONFIG["keyboard"]["background-color"]}
            """,
        )

    def generate_keyboard(self):
        for i, row in enumerate(self.matrix):
            layout = QHBoxLayout()
            for word in row:
                btn = QPushButton(self)
                btn.setFont(self.font)
                btn.size()
                if i == 4:
                    if word == "space":
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
                # btn.clicked.connect(self.clicked_on_btn)
                size_policy = btn.sizePolicy()
                size_policy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(size_policy)
                layout.addWidget(btn)
                keyboard_btn[word] = btn
            self.keyboard_layout.addLayout(layout)

        self.plain_text_edit_1 = MyPlainTextEdit(self)
        self.plain_text_edit_1.setStyleSheet(self.source_plain_text_edit_1.styleSheet())
        self.plain_text_edit_1.setFont(self.font)
        self.texts_layout.replaceWidget(self.source_plain_text_edit_1, self.plain_text_edit_1)
        self.source_plain_text_edit_1.close()
        self.plain_text_edit_1.textChanged.connect(self.translate)

    def translate(self):
        self.plain_text_edit_2.setPlainText('')
        for word in self.plain_text_edit_1.toPlainText():
            if word in anbur:
                self.plain_text_edit_2.insertPlainText(anbur[word])
            else:
                self.plain_text_edit_2.insertPlainText(word)
