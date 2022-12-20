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
## 计算jar文件MD5值
with open('HenryQin.jar', 'rb') as i:
    m = hashlib.md5(i.read()).hexdigest()


# spider替换
data1=re.sub('"spider":.*",', '"spider":"https://henryqinup.github.io/JK/HenryQin.jar;md5;'+m+'",', data, count=1, flags=re.M)
# wallpaper替换
data2=re.sub('"wallpaper": "http://101.34.67.237/pics",', '"wallpaper":"https://henryqinup.github.io/JK/background.jpg",', data1, count=1, flags=re.M)
# 提取需要的站点
sitelibvio=re.compile('({(\s*)|(\n)"key":\s*"dr_LIBVIO",\s*.*?},\s*)',flags=re.S|re.I).search(data).group(4)
sitebuka=re.compile('({\s*"key":\s*"dr_真不卡",\s*.*?},\s*)',flags=re.S|re.I).search(data).group()

## 更改站点顺序
add=sitelibvio+sitebuka
data3=re.sub('"sites":.\[\n', '"sites": [\n'+'    '+add,data2, count=1,flags=re.S|re.I)
with open("jarurl.txt", "a+",encoding='UTF-8') as out_file:
    out_file.write('\n'+add)

# 解析设置轮询并发优先
#lunxun=re.compile('({\n            "name": "轮询",\n            "type": 2,\n            "url": "Sequence",\n            "header": {\n                "User-Agent": "Mozilla/5.0"\n            }\n        },\n        {\n            "name": "并发",\n            "type": 2,\n            "url": "Parallel",\n            "header": {\n                "User-Agent": "Mozilla/5.0"\n            }\n        },\n)',flags=re.S|re.I).search(data).group()
#parses=re.compile('({\n            "key": "dr_LIBVIO",\n.*?},\n)',flags=re.S|re.I).search(data).group()
data4=re.sub('{\n            "name": "🌐Ⓤ",\n            "type": 0,\n            "url": "",\n            "header": {\n                "User-Agent": "Mozilla/5.0"\n            }\n        },\n','', data3, count=1,flags=0)
##添加web和json聚合解析
#juhe='{\n		"name": "Json\u805a\u5408",\n		"type": 3,\n		"url": "Demo"\n	},\n {\n		"name": "Web\u805a\u5408",\n		"type": 3,\n		"url": "Web"\n	},\n'
#data5=re.sub('"parses": [\n', '"parses": [\n'+juhe, data4, count=1,flags=re.S|re.I)

localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open("Q2WForever.json", "w",encoding='UTF-8') as out_file:
    out_file.write('// https://henryqinup.github.io/JK/Q2WForever.json '+localtime+'\n'+data4)
