from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# 设置了环境变量还是不行，直接采用终极办法绝对路径
driver.get('http:\\www.baidu.com')
