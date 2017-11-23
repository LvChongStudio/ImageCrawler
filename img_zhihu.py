import os
import re
import requests
def download(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+folder+'/'+name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False

header = {'User-Agent':'studio_agent'}

errs=[]

def fetch(url):
    r = requests.get(url,headers=header)
    text= r.text
    imgs=[]

    # jpg = re.compile(r'https://[^\s]*?\.jpg')
    # jpeg = re.compile(r'https://[^\s]*?\.jpeg')
    # gif = re.compile(r'https://[^\s]*?\.gif')
    # png = re.compile(r'https://[^\s]*?\.png')

    jpg = re.compile(r'https://[^\s]*?_r\.jpg')
    jpeg = re.compile(r'https://[^\s]*?_r\.jpeg')
    gif = re.compile(r'https://[^\s]*?_r\.gif')
    png = re.compile(r'https://[^\s]*?_r\.png')

    imgs+=jpg.findall(text)
    imgs+=jpeg.findall(text)
    imgs+=gif.findall(text)
    imgs+=png.findall(text)


    errors = []

    folder = url.split('/')[-1]
    for img_url in imgs:
        if download(folder,img_url):
            print("download :"+img_url)
        else:
            errors.append(img_url)
    return errors
# 22212644   29814297    31983868   20399991
urls=['https://www.zhihu.com/question/22212644']
for url in urls :
    print(url)
    errs+=fetch(url)

print("ERROR URLS:")
print(errs)
print os.path