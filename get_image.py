import requests
import os

def download_img(url):
    '''获取每张图片的内容'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':'keep-alive',
        'Host': 'puui.qpic.cn',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    # 这个头别到处乱抄，最好还是自己用一次复制下来
    img = requests.get(url,headers=headers).content
    return img

def get_img(img_url):
    '''下载图片'''
    img_file_name = r"C:\Users\hh\Desktop\selenium.png"
    if os.path.exists(img_file_name):
        os.remove(img_file_name)
    else:
        pass
    img = download_img("http:" + img_url)
    with open(img_file_name,'wb') as f:
        f.write(img)

# get_img(r"//puui.qpic.cn/qqvideo_ori/0/h00318f7lem_228_128/0")


