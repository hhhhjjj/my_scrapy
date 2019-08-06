from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, timedelta


def parser_page():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    texts = soup.find_all("div", class_="WB_text W_f14")
    print(texts)


def find_element(the_str):
    while True:
        if driver.page_source.find(the_str) != -1:
            # 这个打印出来知道是不等于1的，所以需要用不等于-1的情况
            break
        else:
            time.sleep(1)
            continue


def judge_time():
    # 范围时间
    d_time = datetime.strptime('2019-08-05' + '15:20', '%Y-%m-%d%H:%M')
    d_time1 = datetime.strptime('2019-08-07' + '15:30', '%Y-%m-%d%H:%M')
    # 当前时间
    n_time = datetime.now()

    if d_time < n_time < d_time1:
        pass
    else:
        while True:
            print("time false")


judge_time()
input_username = input("账号：")
input_password = input("密码：")
read_num = 0
trans = 0
comment = 0
like = 0
chrome_option = Options()
# chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
                          , options=chrome_option)
driver.get("https://weibo.com/")
driver.maximize_window()
find_element('info_list login_btn')
driver.find_element_by_id("loginname").send_keys(input_username)
driver.find_element_by_name("password").send_keys(input_password)
driver.find_element_by_xpath("//div[@class='info_list login_btn']").click()
find_element('gn_name')
print("login sucess")
driver.find_element_by_xpath("//a[@class='gn_name']").click()
find_element('bar_title')
username = driver.find_element_by_xpath("//h1[@class='username']").text
text_pattern  = "//div[@class='WB_text W_f14' and @node-type = 'feed_list_content']"
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

texts = driver.find_elements_by_xpath(text_pattern)
like_and_comment = driver.find_elements_by_xpath("//ul[@class='WB_row_line WB_row_r4 clearfix S_line2']")
publish_times = driver.find_elements_by_xpath("//div[@class='WB_from S_txt2']")[1:]
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")[5:].replace("0", "").replace("-", "月") + "日"
for publish_time, the_text, lines in zip(publish_times, texts, like_and_comment):
    if publish_time.text[:-22] == yesterday:
        print(the_text.text[:30])
        i = 0
        for every_line in lines.text.split("\n"):
            if i == 0:
                read_num = int(re.findall(r"\d+\.?\d*", every_line)[0]) + read_num
            elif i == 1:
                every_line = every_line.replace("转发", "0")
                trans = int(re.findall(r"\d+\.?\d*", every_line)[0]) + trans
            elif i == 2:
                every_line = every_line.replace("评论", "0")
                comment = int(re.findall(r"\d+\.?\d*", every_line)[0]) + comment
            elif i == 3:
                every_line = every_line.replace("赞", "0")
                like = int(re.findall(r"\d+\.?\d*", every_line)[0]) + like
            i = i + 1
    else:
        pass

print(read_num)
print(trans)
print(comment)
print(like)



