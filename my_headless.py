# 如果正常浏览的话，比如看评论，只能看到前面几条评论
# 后面的评论需要手动点击加载更多才行
# 点击加载一般是再做一次请求，但是我们不想去解析那些js代码
# 一种方法就是解析那个加载更多，来找规则，太麻烦了
# 第二种方法就是带上浏览器，让浏览器去解析js代码，我们用selenium
# 现在很多网页都是动态ajax，直接抓取html源代码行不通
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys


chrome_option = Options()
chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
                          , options=chrome_option)
driver.get("http://116.230.161.59:8090/byebye/")
tag = driver.find_element_by_id("id_btn")
tag.click()
i = 0
while True:
    try:
        driver.find_element_by_id("id_bluebox")
        break
    except:
        time.sleep(1)
        i = i + 1
        print(i)
        continue
print("ok")

# driver方法比较慢，有的公司要求速度快的还是要去解析js规则

# 这个selenium还能执行js代码，能拉滚动条这些
# 比如selenium点击按键，然后就相当于执行了js，然后我们再来获取page_source
# 有的如果设置了延时生成，或者网络不好，我们就试着查，一直循环查到再继续进行下去

# 有的反爬特别恶心，一个页面里面显示的其实是在子页面里面，结果selenium找不到元素
# 这时候先找到对应的控件，然后从控件进去找

# 有的进去之后还会进行替换，反正各种麻烦
# selenium有特殊的字段，有的网站反爬能找到，这时候需要找到二进制字段自己来改

# 爬腾讯视频不用怕重复的， 腾讯已经替你筛选过了
# 注意爬的时候一定要一直向下拉，不然出来的图片是腾讯的log，只有向下拉之后才会换成真实的图片


