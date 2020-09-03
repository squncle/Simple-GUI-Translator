from settings import TENCENT
import requests
import time
import random
import urllib.parse
import hashlib


class Tencent:
    def __init__(self):
        self.api = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate"
        self.app_id = TENCENT['app_id']
        self.app_key = TENCENT['app_key']
        self.to_langs = {
            '中文': 'zh',
            '英语': 'en',
            '日语': 'jp',
            '韩语': 'kr',
        }

    def translate(self, text, from_lang, to_lang, mysignal):
        params = {
            'app_id': int(self.app_id),
            'nonce_str': str(random.randint(12345, 54321)),
            'source': from_lang,
            'target': to_lang,
            'text': text,
            'time_stamp': int(time.time()),
        }
        str_T = urllib.parse.urlencode(params)
        str_S = str_T + f"&app_key={self.app_key}"

        # 签名
        md5 = hashlib.md5()
        md5.update((str_S).encode())
        sign = md5.hexdigest()
        params.update({'sign': sign.upper()})

        res = requests.get(self.api, params=params)
        res_json = res.json()
        src = res_json['data']['source_text']
        dst = res_json['data']['target_text']
        mysignal.text_print.emit(src, dst)
