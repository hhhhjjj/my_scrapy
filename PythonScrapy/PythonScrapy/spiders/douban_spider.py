# scrapy crawl douban_movie_top250 -o douban.csv
# spider就是用来抓取信息的，定义用于下载url列表，跟踪链接的方案，解析网页的方式
# 用来提取items
import scrapy
from PythonScrapy.items import PythonscrapyItem
# 就是这个样子用，因为你操作cmd的时候这样才能找到
# spiders生成request，然后传到downloader执行request返回response给spiders

class douban_spider(scrapy.Spider):
    name = 'douban_movie_top250'
    start_url = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        # 这个函数必须返回可迭代对象，对象包含用于爬取的第一个request
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)
    #     注意这个是在scrapy里面

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

