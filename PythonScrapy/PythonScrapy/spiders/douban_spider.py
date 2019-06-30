# 在这不能直接用scrapy crawl douban这个命令
# 要进如PythonScrapy这个文件夹里面才可以用这个命令
# spider就是用来抓取信息的，定义用于下载url列表，跟踪链接的方案，解析网页的方式
# 用来提取items
import scrapy


class douban_spider(scrapy.Spider):
    name = 'douban_spider'
    def start_requests(self):
        start_url=''