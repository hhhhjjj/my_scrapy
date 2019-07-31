import win32gui
import time
import win32api
import win32con
import get_image
import pymongo
from selenium.webdriver.common.action_chains import ActionChains
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
driver.find_element_by_name("account").send_keys("1094231447@qq.com")
driver.find_element_by_name("password").send_keys("hjk1996829")
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
all_windows = driver.window_handles
driver.switch_to.window(all_windows[2])
# 注意这里又弹出了新的窗口，所以需要改，不然会一直报错找不到
find_element("请在这里输入标题")


def windows_operate():
    # use win32gui and spy++ to select windows and picture
    time.sleep(0.5)
    while True:
        if win32gui.FindWindow(None, "打开") != 0:
            break
        else:
            continue
    window_handle = win32gui.FindWindow(None, "打开")
    ComboBoxEx32 = win32gui.FindWindowEx(window_handle, 0, 'ComboBoxEx32', None)
    # 中间有个这个，特别难找到
    combobox_handle = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", "")
    edit_handle = win32gui.FindWindowEx(combobox_handle, 0, "Edit", None)
    win32gui.SendMessage(edit_handle, win32con.WM_SETTEXT, None, r'C:\Users\hh\Desktop\selenium.png')
    # 往输入框输入绝对地址
    open_button = win32gui.FindWindowEx(window_handle, 0, 'Button', None)
    win32gui.SendMessage(window_handle, win32con.WM_COMMAND, 1, open_button)
    # 按button


def write_one(title, image, href):
    get_image.get_img(image)
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)
    driver.find_element_by_xpath('//*[@id="author"]').send_keys("James He")
    # 不允许正文直接插入链接
    time.sleep(0.5)
    driver.find_element_by_xpath('//iframe[@id="ueditor_0"]').click()
    time.sleep(0.5)
    driver.find_element_by_id("js_editor_insertimage").click()
    # find_element('ul class="tpl_dropdown_menu edui-default" style=""')
    # 这样子才能确定下拉菜单显示出来了
    time.sleep(0.5)
    driver.find_element_by_xpath("//input[@class = ' edui-default']").click()
    # 这个有空格要注意
    windows_operate()
    js = "var q=document.documentElement.scrollTop=1200"
    time.sleep(0.5)
    driver.execute_script(js)
    driver.find_element_by_id("js_cover_area").click()
    driver.find_element_by_id("js_imagedialog").click()
    find_element("本地上传")
    driver.find_element_by_xpath("//span[@class = 'upload_area webuploader-container']").click()
    # 这个上传的id总是变，不能用id定位

    windows_operate()
    # 上传完成之后要等图片加载出来，不然会提示选择裁切区域
    time.sleep(0.5)
    find_element("weui-desktop-step current ")
    driver.find_element_by_xpath("//span[@class = 'js_crop_done_btn btn btn_primary btn_input js_btn_p']").click()
    while True:
        time.sleep(1)
        if driver.page_source.find("剪裁封面") == -1:
            # 这个打印出来知道是不等于1的，所以需要用不等于-1的情况
            break
        else:
            driver.find_element_by_xpath(
                "//span[@class = 'js_crop_done_btn btn btn_primary btn_input js_btn_p']").click()
            continue
    # 阅读原文插入链接
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[@class = 'allow_click_opr js_article_url_allow_click']").click()
    driver.find_element_by_xpath("//input[@class = 'weui-desktop-form__input js_url js_field']").send_keys(href)
    driver.find_element_by_xpath("//a[@class = 'btn btn_primary jsPopoverBt']").click()
    print("完成一篇")
    time.sleep(0.5)


def create_new():
    driver.execute_script("document.getElementById('js_mp_sidemenu').scrollTop=1200")
    driver.find_element_by_xpath("//div[@class = 'preview_media_add_wrp js_readonly']").click()
    # 下拉侧边框
    driver.find_element_by_xpath("//li[@class = 'js_create_article' and @data-type = '0']").click()


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tx_video_db"]
# 创建一个数据库,要注意只有插入内容之后才会真的创建出来
video = mydb["video"]

text_number = 0
for a_video in video.find():
    write_one(a_video["title"], a_video["image"], a_video["href"])
    text_number = text_number + 1
    if text_number > 2:
        break
    else:
        while True:
            time.sleep(1)
            try:
                create_new()
                break
            except:
                continue
# 原创声明这个懒得弄了

# driver.find_element_by_xpath("//span[@class = 'btn btn_input btn_default r']").click()
# # 发送特别麻烦，还要各种扫码，后面的都一个套路，不弄了


