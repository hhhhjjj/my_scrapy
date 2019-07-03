# 在这不能直接用scrapy crawl douban这个命令
# 要进如PythonScrapy这个文件夹里面才可以用这个命令
# spider就是用来抓取信息的，定义用于下载url列表，跟踪链接的方案，解析网页的方式
# 用来提取items
import scrapy
from PythonScrapy.PythonScrapy.items import PythonscrapyItem


class douban_spider(scrapy.Spider):
    name = 'douban_movie_top250'
    start_url = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = PythonscrapyItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        # xpath是在xml里面查找信息的语言
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            # 在这不要用ur，太老了，用r就行了
            yield item

