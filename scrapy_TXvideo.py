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


def scroll():
    driver.set_window_size(1000, 1000)
    # 这个需要把浏览器窗口大小设置的比较大，这样子才能翻页找到下一页
    # 不然会被挡住找不到的

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
    parser_page()
    next_page()


def parser_page():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all("li", class_="list_item")
    for item in range(len(titles)):
        # print(titles[item])
        title = titles[item].img.get('alt', '')
        image = titles[item].img.get('src', '')
        href = titles[item].a.get('href', '')
        my_mongodb.add_video(title, image, href)


def next_page():
    # 翻页
    # driver.save_screenshot('video.png')
    # 找不到原因就截个图看看
    if driver.page_source.find("page_next disabled") == -1:
        driver.find_element_by_class_name("page_next").click()
        print("下一页")
        scroll()
    else:
        print("结束")


scroll()

