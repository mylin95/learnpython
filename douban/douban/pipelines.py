# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from douban.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection


class DoubanPipeline:
    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        sheet_name = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        my_db = client[db_name]
        self.post = my_db[sheet_name]
    
    # 数据插入
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
