import requests
import re
import time
import random
import hashlib

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
headers = {'Referer': 'http://fanyi.youdao.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
           }

def fanyi_youdao():
    while True:
        content = input('请输入要翻译的词:')
        if content == 'exit':return None
        data= {}
        u = 'fanyideskweb'
        d = content
        f = str(int(time.time()*1000) + random.randint(1,10))
        c = "rY0D^0'nM0}g5Mm1z%1G4"
        sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

        data['i'] = content
        data['form'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dice'
        data['client'] = 'fanyideskweb'
        data['salt'] = f
        data['sign'] = sign
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data['typoResult'] = 'true'

        html = requests.post(url=url,data=data,headers=headers)
        rule = re.compile(r'"tgt":"(.*?)",')
        result = re.search(rule,html.text).group(1)
        print(result)

if __name__ == "__main__":
    fanyi_youdao()


