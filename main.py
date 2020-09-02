from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import Signal, QObject

import trans


engines = {
    '百度翻译': trans.Baidu(),
}

to_langs = {
    '中文': 'zh',
    '英语': 'en',
    '日语': 'jp',
    '韩语': 'kor',
}


class MySignal(QObject):
    text_print = Signal(str, str)


class Translator:
    def __init__(self):
        self.ui = QUiLoader().load('translator.ui')
        self.ms = MySignal()
        self.clipboard = QGuiApplication.clipboard()

        # 默认百度翻译、源语言自动识别、目标语言中文
        self.engine = trans.Baidu()
        self.from_lang = 'auto'
        self.to_lang = 'zh'

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
        self.to_lang = to_langs[self.ui.comboBox_3.currentText()]

    def automatically_translate(self):
        text = self.clipboard.text()
        self.engine.translate(text, self.from_lang, self.to_lang, self.ms)

    def manually_translate(self):
        text = self.ui.plainTextEdit.toPlainText()
        self.engine.translate(text, self.from_lang, self.to_lang, self.ms)


app = QApplication([])
translator = Translator()
translator.ui.show()
app.exec_()
