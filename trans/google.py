import execjs
import requests


class Google:
    def __init__(self):
        self.api = "https://translate.google.cn/translate_a/single"
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
    
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
        """)
        self.to_langs = {
            '中文': 'zh-CN',
            '英语': 'en',
            '日语': 'ja',
            '韩语': 'ko',
        }

    def get_TK(self, text):
        """
        获取TK值
        """
        return self.ctx.call("TL", text)

    def translate(self, text, from_lang, to_lang, mysignal):
        params = {
            "client": "webapp",
            "sl": from_lang,
            "tl": to_lang,
            "hl": from_lang,
            "dt": "at",
            "dt": "bd",
            "dt": "ex",
            "dt": "ld",
            "dt": "md",
            "dt": "qca",
            "dt": "rw",
            "dt": "rm",
            "dt": "ss",
            "dt": "t",
            "swap": 1,
            "otf": 2,
            "ssel": 5,
            "tsel": 5,
            "kc": 1,
            "tk": self.get_TK(text),
            "q": text
        }
        res = requests.get(self.api, params=params)
        res_json = res.json()

        # 合并分段翻译
        src = []
        dst = []
        for lines in res_json[0]:
            src.append(lines[1])
            dst.append(lines[0])
        src = "".join(src)
        dst = "".join(dst)
        mysignal.text_print.emit(src, dst)
