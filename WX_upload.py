import win32gui
import time
# 这个库能够界面图形化操作，不用通过像素点来点击，可以通过窗口，按键这些来
# 比如找到当前弹出的窗口里面找到选择文件的窗口，然后找到文本框，然后找到确定按键
# 可以下载个spy++来找到窗口还有控件的名字
# 有的页面切换没这么快，你点了下一个，结果还是之前的，你就开始新的点击了
# 所以需要仔细看区别，有的点击成功之后会出现selected，就可以了
# 尽量不要用sleep，有时候网速不好
# ajax是异步请求，不会等后端的，它提取操作了
# wx这个cookie有效期就一天，所以加载cookie没什么用
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
# chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
                          , options=chrome_option)
driver.get("https://mp.weixin.qq.com")
driver.maximize_window()
driver.find_element_by_name("account").send_keys("")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_class_name("btn_login").click()
time.sleep(5)
# wx的cookie只能一天，所以还是手动扫码吧


def find_element(the_str):
    while True:
        if driver.page_source.find(the_str) != -1:
            # 这个打印出来知道是不等于1的，所以需要用不等于-1的情况
            break
        else:
            time.sleep(1)
            continue


find_element("帐号整体情况")
js = "var q=document.documentElement.scrollTop=50"
driver.execute_script(js)
home_window = driver.current_window_handle
driver.find_element_by_xpath("//a[@class='weui-desktop-btn weui-desktop-btn_primary']").click()
# 这种多个class的需要这样做，或者只选择其中一个class
# 注意要用element，不然是返回列表
# 注意这里这个class被用了不止一次，所以会报错
# 最后还是用xpath吧
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])
time.sleep(0.5)
find_element("create-type__link js_MsgSenderLinkBt")
driver.find_element_by_css_selector(".create-type__link.js_MsgSenderLinkBt").click()
time.sleep(0.5)
find_element("title")
driver.find_element_by_name("title").click()
driver.find_element_by_name("title").send_keys("selenium login and write")
driver.find_element_by_id("author").send_keys("James He")
driver.find_element_by_id("edui1_contentplaceholder").send_keys("https://github.com/hhhhjjj/my_scrapy")
driver.find_element_by_class_name("icon_media_choose edui-default").click()
driver.find_element_by_class_name("edui-default").click()
