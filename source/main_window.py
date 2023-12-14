from PyQt5.QtGui import QFontDatabase, QFont, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QPlainTextEdit, QApplication

from source.anbur import anbur
from source.config import CONFIG
from source.design import Ui_MainWindow

keyboard_btn = dict()


class MyPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super(MyPlainTextEdit, self).__init__(parent)

    def keyPressEvent(self, event):
        key = event.text().lower()
        print(event.key())
        if key in keyboard_btn:
            keyboard_btn[key].animateClick()
        super(MyPlainTextEdit, self).keyPressEvent(event)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont('fonts/Everson Mono.ttf')

        self.setWindowTitle("Анбур Переводчик скачать бесплатно на русском бутстрап торрент")

        self.font = QFont('Everson Mono')
        self.font.setPointSize(20)
        self.plain_text_edit_2.setFont(self.font)
        self.matrix = [
            ['ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
            ['tab', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', '\\'],
            ['capslock', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'enter'],
            ['shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', 'shift'],
            ['Ctrl', 'Win', 'Alt', 'space', 'Alt', 'Ctrl'],
        ]
        self.generate_keyboard()

        self.set_initial_stylesheets()

    def set_initial_stylesheets(self):
        self.setStyleSheet(
           f"""
           #frame {{
                border-radius: 4px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]}
           }}
            QMainWindow {{
                background-color: {CONFIG["keyboard"]["background-color"]};
            }}
            QLabel {{
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]}
            }}
            QMenuBar {{
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]}
            }}
            QMenuBar::item {{
                spacing: 0px;
                margin-top: 1px;
                padding: 3px 8px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["border-color"]};
                width: 64px;
                height: 25px;
            }}
            QMenuBar::item:selected {{
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["active"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["active"]};
            }}
            """

        )
        self.frame_2.setStyleSheet(
            f"""
            background-color: {CONFIG["keyboard"]["background-color"]};
            """,
        )
        self.plain_text_edit_1.setStyleSheet(
            f"""
            QPlainTextEdit {{
                padding: 4px;
                border-radius: 4px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            QPlainTextEdit:focus {{
                padding: 4px;
                border-radius: 4px;
                border: {CONFIG["keyboard"]["border"]};
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            """
        )
        self.plain_text_edit_2.setStyleSheet(
            f"""
            QPlainTextEdit {{
                padding: 4px;
                border-radius: 4px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            QPlainTextEdit:focus {{
                padding: 4px;
                border-radius: 4px;
                border: {CONFIG["keyboard"]["border"]};
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            """
        )
        self.reverse_translate_btn.setStyleSheet(
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

    def generate_keyboard(self):
        for i, row in enumerate(self.matrix):
            layout = QHBoxLayout()
            for word in row:
                btn = QPushButton(self)
                btn.setFont(self.font)
                btn.size()
                if word in ["tab", "capslock", "shift", "Ctrl", "backspace", "enter"]:
                    btn.setMaximumSize(300, 60)
                    btn.setMinimumHeight(60)
                    btn.setText(anbur[word]) if word in anbur else btn.setText(word)
                else:
                    if i == 4:
                        if word == "space":
                            w, h = 330, 60
                        else:
                            w, h = 90, 60
                            btn.setText(word)
                        btn.setMaximumSize(w, h)
                        btn.setMinimumSize(w, h)
                    else:
                        btn.setText(anbur[word]) if word in anbur else btn.setText(word)
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
            self.plain_text_edit_2.insertPlainText(
                anbur[word.lower()].upper()) if word.isupper() else self.plain_text_edit_2.insertPlainText(
                anbur[word]) if word.lower() in anbur else self.plain_text_edit_2.insertPlainText(word)
