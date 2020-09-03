from settings import BAIDU
import requests
from random import randint
import hashlib


class Baidu:
    def __init__(self):
        self.api = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.appid = BAIDU['appid']
        self.appsecret = BAIDU['appsecret']
        self.to_langs = {
            '中文': 'zh',
            '英语': 'en',
            '日语': 'jp',
            '韩语': 'kor',
        }

    def translate(self, text, from_lang, to_lang, mysignal):
        params = {
            'q': text,
            'from': from_lang,
            'to': to_lang,
            'appid': self.appid,
            'salt': str(randint(12345, 54321)),
        }

        # 签名
        md5 = hashlib.md5()
        md5.update((self.appid + params['q'] + params['salt'] + self.appsecret).encode())
        sign = md5.hexdigest()
        params.update({'sign': sign})

        res = requests.get(self.api, params=params)
        res_text = res.json()
        src = res_text['trans_result'][0]['src']
        dst = res_text['trans_result'][0]['dst']
        mysignal.text_print.emit(src, dst)
