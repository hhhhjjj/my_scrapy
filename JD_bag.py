# 爬京东书包
import requests
# 注意有个s在后面
from bs4 import BeautifulSoup
# 如果网站出现变动，正则表达式就需要修改，bs就好许多，现在一般用正则表达式的也少了
# from http import cookiejar
# # py2是直接导入cookielib，py3这改成这样子了
# from urllib import request
# cj = cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cj)
# # 这个也是要改成这样子才能找到。请求中的cookie会自动存储到cj中，当然这个也可以存到本地
# opener = request.build_opener(handler)


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
# headers里面可以直接加上手动访问成功的cookie，在一些比较垃圾的网站就可以直接访问进去了
# 就不用每次都登陆了

def get_text(url):
    r = requests.get(url, headers=headers)
    # 登陆注册用post也行，记得带上data
    # html = opener.open(request).read().decode('utf-8')
    # 要用上cookie就要用这个方法来发送请求
    r.encoding = 'utf-8'
    # requests会自动推测编码的，不写这个也行
    r.raise_for_status
    # 如果有异常这就是抛出异常用的
    return r.text


def get_info(text, title, price):
    soup = BeautifulSoup(text, 'html.parser')
    # 后面这些用开发者模式来看就能找到
    # 不过表示京东的比较好找
    names = soup.find_all("div",class_="p-name p-name-type-2")
    prices = soup.find_all("div", class_="p-price")
    for i in range(len(names)):
        # 后面.什么是树状结构的，name里面<a>里面再<em>里面的，就是我们要的文本了
        title.append(names[i].a.em.text)
        price.append(prices[i].strong.i.text)


def print_info(names, prices):
    t="{0:^3}\t{1:^8}\t{2:^50}"
    # 格式化字符串打印，：是格式限定符
    # ^是居中，后面的数字是宽度
    for i in range(len(names)):
        print(t.format(i+1,prices[i],names[i]))


url = "https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=%E4%B9%A6%E5%8C%85&pvid=cacd21b19bb746d4927aae1ea15028e2 "
name = []
price = []
get_info(get_text(url), name, price)
print_info(name, price)
# 遇到登陆页面的
# 不一定要selenium，有的小网站你知道开发方式，用post或者get方式也能登陆
# 去network里面看提交的方式这些
# 有的大网站也有本事用get来提交的，自己有办法加密，一定要带上他们自己加上的东西
# 然后多试试找出规律
# 验证码这种，我们先手动一次，拿到cookie
# 之后就用这个cookie了，别死磕图像识别
# 有的比较麻烦的，不同时刻密码不同的
# 这种要带上时间戳提交，一点点猜
# 有的登陆写到js里面，而不是写到表单里面，要一点点找
# 反正就是先手动登陆一次，看服务器需要什么，对比着找
# 要么改cookie，要么改session
# cookie在浏览器，session在服务器
# 服务器根据客户端来的session_id去查数据库里面的session表，看是否登陆过
# 拿到cookie就没有安全性可言了

