from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import Signal, QObject
from translator_ui import Ui_Form
import os

import trans


# 设置环境变量
dirname = os.path.dirname(__file__)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(dirname, 'platforms')

engines = {
    '谷歌翻译': trans.Google(),
    '有道翻译': trans.Youdao(),
}


class MySignal(QObject):
    text_print = Signal(str, str)


class Translator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ms = MySignal()
        self.clipboard = QGuiApplication.clipboard()

        # 默认谷歌翻译、源语言自动识别、目标语言中文
        self.engine = engines['谷歌翻译']
        self.from_lang = 'auto'
        self.to_lang = 'zh-CN'
        self.to_langs = self.engine.to_langs

        self.clipboard.dataChanged.connect(self.automatically_translate)
        self.ui.pushButton.clicked.connect(self.manually_translate)
        self.ms.text_print.connect(self.print_to_gui)
        self.ui.comboBox.currentIndexChanged.connect(self.check_options)
        self.ui.comboBox_3.currentIndexChanged.connect(self.check_options)

    def print_to_gui(self, src, dst):
        self.ui.plainTextEdit.setPlainText(src)
        self.ui.plainTextEdit_2.setPlainText(dst)

    def check_options(self):
        self.engine = engines[self.ui.comboBox.currentText()]
        self.to_langs = self.engine.to_langs
        self.to_lang = self.to_langs[self.ui.comboBox_3.currentText()]

    def automatically_translate(self):
        text = self.clipboard.text()
        self.engine.translate(text, self.from_lang, self.to_lang, self.ms)

    def manually_translate(self):
        text = self.ui.plainTextEdit.toPlainText()
        self.engine.translate(text, self.from_lang, self.to_lang, self.ms)


app = QApplication([])
translator = Translator()
translator.show()
app.exec_()
