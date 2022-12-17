import re
import requests
import time
import hashlib

f = open("jk0.txt", "wb")
conten = requests.get('http://drpy.site/js0')  # 读取网页内容
conten1=conten.content
f.write(conten1)
f.close()

with open("jk0.txt", encoding='utf8') as g:
    data = g.read() #需要改的内容

# 获取jar的url地址,并将地址写入jarurl.txt
searchjarurl=re.search('("spider":.*")(http.*)(.*")',data,flags=re.M)
jarurl=searchjarurl.group(2)
with open("jarurl.txt", "w",encoding='UTF-8') as out_file:
    out_file.write(jarurl)
# 将获取到的jar内容写入HenryQin.jar
h = open("HenryQin.jar", "wb")
conten2 = requests.get(jarurl)  # 读取网页内容
conten3=conten2.content
h.write(conten3)
h.close()
    # 计算jar文件MD5值
with open('HenryQin.jar', 'rb') as i:
    m = hashlib.md5(i.read()).hexdigest()


# spider替换
data1=re.sub('"spider":.*",', '"spider":"https://henryqinup.github.io/JK/HenryQin.jar;md5;'+m+'",', data, count=1, flags=re.M)
# wallpaper替换
data2=re.sub('"wallpaper": "http://101.34.67.237/pics",', '"wallpaper":"https://henryqinup.github.io/JK/background.jpg",', data1, count=1, flags=re.M)
# 提取需要的站点，并且更改站点顺序
searchsite=re.search('({\n            "key":"dr_LIBVIO",\n            "name": "LIBVIO\(drpy\)",\n)',data,flags=re.S|re.I)
sitelibvio=searchsite.group(1)
with open("jarurl.txt", "a+",encoding='UTF-8') as out_file:
    out_file.write('\n'+sitelibvio)
data3=re.sub('"sites":.\[\n', '"sites": [\n'+'    '+sitelibvio,data2, count=1, flags=re.M|re.I)
#负载均衡设置
#data4=re.sub('strategy: consistent-hashing', 'strategy: round-robin', data3, count=1, flags=0)
# 设置 DNS 经过代理

#data5=re.sub('external-controller: :9090\ndns:\n  enabled: true\n  nameserver:\n    - 119.29.29.29\n    - 223.5.5.5\n  fallback:\n    - 8.8.8.8\n    - 8.8.4.4\n    - tls://1.0.0.1:853\n    - tls://dns.google:853\n', "external-controller: :9090\ntcp-concurrent: true\nipv6: false\ndns:\n  enabled: true\n  ipv6: false \n  listen: 0.0.0.0:53\n  default-nameserver:\n    - 223.5.5.5\n    - 119.29.29.29\n    - 1.1.1.1\n  enhanced-mode: fake-ip\n  fake-ip-range: 198.18.0.1/16 \n  use-hosts: true \n  fake-ip-filter:\n    - '*.lan'\n    - localhost.ptlogin2.qq.com\n  nameserver:\n    - 'https://223.5.5.5/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://doh.pub/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://doh.360.cn/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://dns.alidns.com/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n  fallback:\n    - 'https://dns.google/dns-query#\u2601 国外故障转移'\n    - 'https://1.1.1.1/dns-query#\u2601 国外故障转移'\n    - 'https://cloudflare-dns.com/dns-query#\u2601 国外故障转移'\n    - 'https://doh.opendns.com/dns-query#\u2601 国外故障转移'\n  fallback-filter:\n    geoip: true\n    geoip-code: CN\n    ipcidr:\n      - 240.0.0.0/4\n", data4, count=1, flags=0)

localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open("Q2WForever.json", "w",encoding='UTF-8') as out_file:
    out_file.write('// https://henryqinup.github.io/JK/Q2WForever.json '+localtime+'\n'+data3)
