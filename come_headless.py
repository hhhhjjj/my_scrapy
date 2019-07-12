from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 爬虫时通常不需要打开浏览器，只需要使用浏览器内核
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                          chrome_options=chrome_options)
# 设置了环境变量还是不行，直接采用终极办法绝对路径
driver.get('http:\\www.baidu.com')
time.sleep(1)
# driver.save_screenshot('baidu.png')
# driver.quit()

# 打印出当前网页的源代码
print(driver.page_source)
driver.close()
