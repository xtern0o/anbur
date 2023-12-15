from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap, QTextCursor, QPalette
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QPlainTextEdit
from PyQt5.QtCore import QSize

from source.anbur import anbur
from source.anbur import cirillic
from source.config import CONFIG, GOOD_LETTERS_1
from source.design import Ui_MainWindow

keyboard_btn = dict()


class CirillicPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super(CirillicPlainTextEdit, self).__init__(parent)
        self.translate_mode = True

    def change_translate_mode(self):
        self.translate_mode = False if self.translate_mode else True

    def get_translate_mode(self):
        return self.translate_mode

    def keyPressEvent(self, event):
        key = event.text().lower()
        if key in keyboard_btn:
            keyboard_btn[key].animateClick()
        if event.text().lower() in anbur and self.translate_mode is False:
            self.insertPlainText(anbur[event.text().lower()])
        else:
            super(CirillicPlainTextEdit, self).keyPressEvent(event)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont('fonts/Everson Mono.ttf')


        self.setWindowTitle("Анбур Переводчик")

        icon = QIcon()
        icon.addPixmap(QPixmap("source/img/arrows.png"), QIcon.Normal, QIcon.Off)
        self.reverse_translate_btn.setIcon(icon)
        self.reverse_translate_btn.setIconSize(QSize(25, 25))

        self.font = QFont('Everson Mono')
        self.font.setPointSize(20)
        self.plain_text_edit_2.setFont(self.font)
        self.plain_text_edit_2.setReadOnly(True)
        self.matrix = [
            ['ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
            ['tab', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', '\\'],
            ['capslock', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'enter'],
            ['shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', 'shift'],
            ['Ctrl', 'Win', 'Alt', 'space', 'Alt', 'Ctrl'],
        ]
        self.reverse_translate_btn.clicked.connect(self.change_window_translate_mode)
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
                padding: 7px;
                border-radius: 4px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            QPlainTextEdit:focus {{
                padding: 7px;
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
                padding: 7px;
                border-radius: 4px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
            }}
            """
        )
        self.reverse_translate_btn.setStyleSheet(
            f"""
            QPushButton {{
                padding: 20px;
                border-radius: 2px;
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};                   
            }}
            QPushButton:hover {{
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["active"]};
            }}
            QPushButton:pressed {{
                background-color: {CONFIG["keyboard"]["key"]["background-color"]["active"]};
            }}
            """
        )
        self.statusBar().setStyleSheet(
            f"""
            color: {CONFIG["keyboard"]["key"]["text-color"]["default"]}
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

        self.plain_text_edit_1 = CirillicPlainTextEdit(self)
        self.plain_text_edit_1.setStyleSheet(self.source_plain_text_edit_1.styleSheet())
        self.plain_text_edit_1.setFont(self.font)
        self.texts_layout.replaceWidget(self.source_plain_text_edit_1, self.plain_text_edit_1)
        self.source_plain_text_edit_1.close()
        self.plain_text_edit_1.textChanged.connect(self.translate_cirillic_to_anbur)

    def translate_cirillic_to_anbur(self):
        self.validate()
        self.plain_text_edit_2.setPlainText('')
        for char in self.plain_text_edit_1.toPlainText():
            if char.isupper():
                self.plain_text_edit_2.insertPlainText(anbur[char.lower()].upper())
            else:
                if char.lower() in anbur:
                    self.plain_text_edit_2.insertPlainText(anbur[char])
                elif char.lower() in GOOD_LETTERS_1 or not char.isalpha():
                    self.plain_text_edit_2.insertPlainText(char)

    def translate_anbur_to_cirillic(self):
        self.validate()
        for char in self.plain_text_edit_1.toPlainText():
            if char in cirillic:
                self.plain_text_edit_2.insertPlainText(cirillic[char])
            elif not char.isalpha():
                self.plain_text_edit_2.insertPlainText(char)

    def validate(self):
        text = self.plain_text_edit_1.toPlainText()
        is_ok = True
        if not len(self.plain_text_edit_1.toPlainText()):
            self.plain_text_edit_2.setPlainText("")
        else:
            char = self.plain_text_edit_1.toPlainText()[-1]
            if char.isalpha() and char.lower() not in GOOD_LETTERS_1 and char not in cirillic:
                is_ok = False
                cursor = self.plain_text_edit_1.textCursor()
                self.plain_text_edit_1.setPlainText(text[:-1])
                cursor.setPosition(0)
                cursor.movePosition(QTextCursor.End)
                self.plain_text_edit_1.setTextCursor(cursor)

        if is_ok:
            self.plain_text_edit_1.setStyleSheet(
                f"""
                QPlainTextEdit {{
                    padding: 7px;
                    border-radius: 4px;
                    background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                    color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
                }}
                QPlainTextEdit:focus {{
                    padding: 7px;
                    border-radius: 4px;
                    border: {CONFIG["keyboard"]["border"]};
                    background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                    color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
                }}
                """
            )
        else:
            self.statusBar().showMessage("[!] Некорректный ввод", 5000)
            self.plain_text_edit_1.setStyleSheet(
                f"""
                QPlainTextEdit {{
                    padding: 7px;
                    border-radius: 4px;
                    background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                    color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
                }}
                QPlainTextEdit:focus {{
                    padding: 7px;
                    border-radius: 4px;
                    border: 2px solid {CONFIG["warning"]["border-color"]};
                    background-color: {CONFIG["keyboard"]["key"]["background-color"]["default"]};
                    color: {CONFIG["keyboard"]["key"]["text-color"]["default"]};
                }}
                """
            )

    def change_window_translate_mode(self):
        self.plain_text_edit_1.change_translate_mode()
        current_mode = self.plain_text_edit_1.get_translate_mode()

        if current_mode:
            self.label.setText("Анбур")
            self.label_2.setText("Кириллица")
            text_before = self.plain_text_edit_1.toPlainText()
            text_after = self.plain_text_edit_2.toPlainText()
            self.plain_text_edit_1.setPlainText(text_after)
            self.plain_text_edit_2.setPlainText(text_before)
            self.plain_text_edit_1.textChanged.connect(self.translate_cirillic_to_anbur)
        else:
            self.label.setText("Кириллица")
            self.label_2.setText("Анбур")
            text_before = self.plain_text_edit_2.toPlainText()
            text_after = self.plain_text_edit_1.toPlainText()
            self.plain_text_edit_1.setPlainText(text_before)
            self.plain_text_edit_2.setPlainText(text_after)
            self.plain_text_edit_1.textChanged.connect(self.translate_anbur_to_cirillic)
