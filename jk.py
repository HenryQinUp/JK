import re
import requests
import time

f = open("jk0.txt", "wb")
conten = requests.get('http://drpy.site/js0')  # 读取网页内容
conten1=conten.content
f.write(conten1)
f.close()

with open("jk0.txt", encoding='utf8') as g:
    data = g.read() #需要改的内容
# spider替换
data1=re.sub('^"spider":.*",$', '"spider":"https://henryqinup.github.io/JK/HenryQin.jar",', data, count=1, flags=re.M)
# ws混淆
data2=re.sub('network: ws, ws-opts: {path:.*}}', 'network: ws, ws-opts: {path: "/", headers: {Host: pull.free.video.10010.com}}}', data1, count=1, flags=0)
# 打开udp
data3=re.sub('alterId: 0, cipher: auto,', 'alterId: 0, udp: true, cipher: auto,', data2, count=1, flags=0)
#负载均衡设置
data4=re.sub('strategy: consistent-hashing', 'strategy: round-robin', data3, count=1, flags=0)
# 设置 DNS 经过代理

data5=re.sub('external-controller: :9090\ndns:\n  enabled: true\n  nameserver:\n    - 119.29.29.29\n    - 223.5.5.5\n  fallback:\n    - 8.8.8.8\n    - 8.8.4.4\n    - tls://1.0.0.1:853\n    - tls://dns.google:853\n', "external-controller: :9090\ntcp-concurrent: true\nipv6: false\ndns:\n  enabled: true\n  ipv6: false \n  listen: 0.0.0.0:53\n  default-nameserver:\n    - 223.5.5.5\n    - 119.29.29.29\n    - 1.1.1.1\n  enhanced-mode: fake-ip\n  fake-ip-range: 198.18.0.1/16 \n  use-hosts: true \n  fake-ip-filter:\n    - '*.lan'\n    - localhost.ptlogin2.qq.com\n  nameserver:\n    - 'https://223.5.5.5/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://doh.pub/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://doh.360.cn/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n    - 'https://dns.alidns.com/dns-query#\U0001F1E8\U0001F1F3 国内故障转移'\n  fallback:\n    - 'https://dns.google/dns-query#\u2601 国外故障转移'\n    - 'https://1.1.1.1/dns-query#\u2601 国外故障转移'\n    - 'https://cloudflare-dns.com/dns-query#\u2601 国外故障转移'\n    - 'https://doh.opendns.com/dns-query#\u2601 国外故障转移'\n  fallback-filter:\n    geoip: true\n    geoip-code: CN\n    ipcidr:\n      - 240.0.0.0/4\n", data4, count=1, flags=0)

localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open("Q2WForever2.json", "w",encoding='UTF-8') as out_file:
    out_file.write('# '+localtime+'\n'+data5)
