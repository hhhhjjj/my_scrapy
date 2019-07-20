from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import my_mongodb
chrome_option = Options()
chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
                          , options=chrome_option)
driver.get("https://v.qq.com/x/list/sports?offset=0&itype=1")

# //i.gtimg.cn/qqlive/images/20150608/pic_h.png这个图片需要拖到底部才会替换成我要的图片
# 页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

time.sleep(1)
while True:
    if driver.page_source.find("//i.gtimg.cn/qqlive/images/20150608/pic_h.png") == 1:
        time.sleep(1)
        continue
    else:
        break

# 开始解析
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles = soup.find_all("li", class_="list_item")
for item in range(len(titles)):
    # print(titles[item])
    title = titles[item].img.get('alt', '')
    image = titles[item].img.get('src', '')
    href = titles[item].a.get('href', '')
    my_mongodb.add_video(title, image, href)



