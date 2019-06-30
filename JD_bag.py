# 爬京东书包
import requests
# 注意有个s在后面
from bs4 import BeautifulSoup
# 如果网站出现变动，正则表达式就需要修改，bs就好许多


# 好歹需要带上个头，不然京东多没面子
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
'Referer': 'https://www.jd.com/',
'DNT': '1',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'TE': 'Trailers',
}

def get_text(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    # requests会自动推测编码的，不写这个也行
    r.raise_for_status
    # 如果有异常这就是抛出异常用的
    print(r.text)

get_text("https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=%E4%B9%A6%E5%8C%85&pvid=cacd21b19bb746d4927aae1ea15028e2 ")
