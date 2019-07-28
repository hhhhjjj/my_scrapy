import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tx_video_db"]
# 创建一个数据库,要注意只有插入内容之后才会真的创建出来
video = mydb["video"]

i = 0
for a_video in video.find():
    print(a_video["href"])
    i = i + 1
    if i > 10:
        break
