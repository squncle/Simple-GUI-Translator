import requests
import time
from random import randint
import hashlib


class Youdao:
    def __init__(self):
        self.api = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.to_langs = {
            '中文': 'zh-CHS',
            '英语': 'en',
            '日语': 'jp',
            '韩语': 'kor',
        }

    def translate(self, text, from_lang, to_lang, mysignal):
        time_stamp = str(int(time.time() * 1000) + randint(1, 10))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

        # 签名
        md5 = hashlib.md5()
        md5.update(f"fanyideskweb{text}{time_stamp}rY0D^0\'nM01g5Mm1z%1G4".encode('utf-8'))
        sign = md5.hexdigest()

        data = {
            'i': text,
            'from': from_lang,  # 'AUTO'
            'to': to_lang,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': time_stamp,
            'sign': sign,
            'ts': '1551506287219',
            'bv': '97ba7c7fb78632ae9b11dcf6be726aee',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'False',
        }
        res = requests.post(self.api, data=data, headers=headers)
        res_json = res.json()

        # 合并分段翻译
        src = []
        dst = []
        for lines in res_json['translateResult']:
            for line in lines:
                src.append(line['src'])
                dst.append(line['tgt'])
        src = "\n".join(src)
        dst = "\n".join(dst)
        mysignal.text_print.emit(src, dst)
