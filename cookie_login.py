# cookie的话一般手动登陆一次就能拿到
# 时间长了cookie会失效的，需要重新登陆
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': 'bid=iDf0tyAI54I; ps=y; ll="118183"; __utmc=30149280; _ga=\
           GA1.2.1325106029.1530404146; _gid=GA1.2.1270378106.1530405800; ue="965454764@qq.com";\
           dbcl2="180531938:E/xiLFShgbg"; ck=UDKl; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C153\
           0409505%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D965454764%2540qq.com\
           %26redir%3Dhttps%253A%252F%252Fwww.douban.com%26source%3DNone%26error%3D1011%22%5D;\
           _pk_id.100001.8cb4=cdbf383efde098e6.1530404145.2.1530409505.1530405796.; _pk_ses.100001.\
           8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1325106029.1530404146.153040\
           4146.1530409505.2; __utmz=30149280.1530409505.2.2.utmcsr=accounts.douban.com|utmccn=(referral)\
           |utmcmd=referral|utmcct=/login; __utmt=1; __utmv=30149280.18053; __utmb=30149280.2.10.1530409505;\
           __yadk_uid=5eZwp3s8j7joGLL911UWJkWQpVQg6IX4'}

url = 'http://www.douban.com'
r = requests.get(url, cookies=cookies, headers=headers)
# cookie直接写进头部也可以
with open('douban_2.txt', 'wb+') as f:
    f.write(r.content)
# 反正就这么个框架，照着来就是了
# 想知道登陆成功没，就找不同
# 比如没登陆的话会要求短信注册，登陆之后你搜索下发现没有短信这两个字
