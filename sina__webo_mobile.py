from selenium import webdriver
import time
import datetime

#全局变量
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

def find_element(the_str):
    while True:
        time.sleep(1)
        if driver.page_source.find(the_str) != -1:
            # 这个打印出来知道是不等于1的，所以需要用不等于-1的情况
            break
        else:
            continue

def judge_time():
    # 范围时间
    d_time = datetime.datetime.strptime('2019-08-05' + '15:20', '%Y-%m-%d%H:%M')
    d_time1 = datetime.datetime.strptime('2019-08-07' + '15:30', '%Y-%m-%d%H:%M')
    # 当前时间
    n_time = datetime.datetime.now()

    if d_time < n_time < d_time1:
        pass
    else:
        while True:
            print("time false")


def loginWeibo():
    driver.get('https://passport.weibo.cn/signin/login')
    find_element("loginName")
    driver.find_element_by_id("loginName").send_keys("18804625056")
    driver.find_element_by_id("loginPassword").send_keys("HJK1996829")
    driver.find_element_by_id("loginAction").click()
    find_element('nav-left lite-iconf lite-iconf-profile')
    print('login sucess')
    driver.find_element_by_xpath("//div[@class='nav-left lite-iconf lite-iconf-profile']").click()



judge_time()
loginWeibo()
find_element('m-btn m-btn-block m-btn-lite-white')
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
driver.find_element_by_xpath("//div[@class='lite-btn-more']").click()
texts = driver.find_elements_by_xpath("//div[@class='weibo-text']")
# 拉到最下面
for the_text in texts:
    print(the_text.text)


