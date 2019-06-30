# scrapy startproject PythonScrapy用这个命令来创建
# 和django的方法类似，思想也是，低耦合度
# item是加载抓取内容的容器
# spider是制作爬虫，pipeline是设计管道存储爬取内容
# 这个能多线程这些
# middlewares是中间加，定义了再请求发送之前可以做的处理
# 比如加cookie，加useragent这些。还有获得响应之后的预处理
