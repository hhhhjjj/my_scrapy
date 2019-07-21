import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tx_video_db"]
# 创建一个数据库,要注意只有插入内容之后才会真的创建出来
video = mydb["video"]


def add_video(video_title, video_image, video_href):
    the_video = {"title": video_title, "image": video_image, "href": video_href}
    # 用插入可能导致重复，在这用更新就行了
    video.update({"title": video_title},{'$set': the_video}, True)
    print(the_video)
# mydict = {"name": "jjj"}
#
# title.insert_one(mydict)
#
# mydb['title'].drop()
# dblist = myclient.list_database_names()
# collist = mydb.list_collection_names()
# print(dblist)
# print(collist)
# mydict1 = {"name": "HHH"}
# title.insert_one(mydict1)
# title.delete_many({})
#
# # 删除后输出
# for x in video.find():
#   print(x)
