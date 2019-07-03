# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 在这构建模型
# 我们想要电影名称，描述，评分和格言
# item是保存结构数据的地方，scrapy可以将解析的结果以字典形式返回
# 但是python中字典缺少结构，大型爬虫系统不方便
# 所以在这类用item
import scrapy


class PythonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
