from settings import CAIYUN
import requests
import json


class Caiyun:
    def __init__(self):
        self.api = "http://api.interpreter.caiyunai.com/v1/translator"
        self.token = CAIYUN['token']
        self.to_langs = {
            '中文': 'auto2zh',
            '英语': 'auto2en',
            '日语': 'auto2ja',  # 目前发现彩云api一个bug，自动识别转日语时，若源语言为中文则转换成功，若源语言为英语转换依然为英语
            '韩语': 'auto2ko',  # 彩云小译暂时只支持中英日三种语言互译，目前不支持韩语
        }

    def translate(self, text, from_lang, to_lang, mysignal):
        data = {
            'source': [text],
            'trans_type': to_lang,
            'request_id': 'demo',
            'detect': True,
        }
        headers = {
            'content-type': "application/json",
            'x-authorization': "token " + self.token,
        }
        res = requests.post(self.api, data=json.dumps(data), headers=headers)
        res_json = res.json()
        src = text
        dst = res_json['target'][0]
        mysignal.text_print.emit(src, dst)
