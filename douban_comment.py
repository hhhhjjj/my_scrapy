# -*-coding:utf-8-*-
import requests
import codecs
from bs4 import BeautifulSoup



def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    req = requests.get(url, headers=headers)
    req.encoding = 'utf-8'
    return req.text


def getComment(url):
    html = getHtml(url)
    soupComment = BeautifulSoup(html, 'html.parser')

    comments = soupComment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')

    return onePageComments


if __name__ == '__main__':
    f = codecs.open('titanic.txt', 'w', 'utf-8')
    # 直接用这个来处理读写中文
    for page in range(10):  # 豆瓣爬取多页评论需要验证。
        url = 'https://movie.douban.com/subject/1292722/comments?start=' + str(20*page) + '&limit=20&sort=new_score&status=P'
        print '第%s页的评论:' % (page+1)
        print url + '\n'

        for i in getComment(url):
            f.write(i)
            print i
        print '\n'
