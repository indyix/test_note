import pymongo
import redis

mongo_username = "senguo_test"
mongo_password = "senguo_mongo"
host = "pftest.senguo.me"
database="admin"

redis_auth = "senguo_redis"

# 或者
# mongodb = pymongo.MongoClient(f'mongodb://localhost:27017/pftest',
#                        serverSelectionTimeoutMS=3000, username='user', password='1')

class MongoCache():
    def __init__(self):
        __mongo_client = pymongo.MongoClient(f'mongodb://{mongo_username}:{mongo_password}@pftest.senguo.me:27017/admin', serverSelectionTimeoutMS=3000)
        self.senguopf = __mongo_client["senguopf"]

    def delete_salesman_ticket_trend_cache(self, docs_query={}):
        collection = self.senguopf["salesman_ticket_trend_cache"]
        collection.delete_many(docs_query)
        return self

    def delete_salesman_rank_cache(self, docs_query={}):
        collection = self.senguopf["salesman_rank_cache"]
        collection.delete_many(docs_query)
        return self

    def delete_goods_sale_rank_cache(self, docs_query={}):
        collection = self.senguopf["goods_sale_rank_cache"]
        collection.delete_many(docs_query)
        return self

    def delete_goods_sale_trend_cache(self, docs_query={}):
        collection = self.senguopf["goods_sale_trend_cache"]
        collection.delete_many(docs_query)
        return self

    def delete_shop_sale_record_cache(self, docs_query={}):
        collection = self.senguopf["shop_sale_record_cache"]
        collection.delete_many(docs_query)
        return self

class RedisCache():
    def __init__(self):
        __redis_client = redis.StrictRedis(host='pftest.senguo.me', port=6379, password='senguo_redis')
        self.rc=__redis_client

    def delete_tj(self, sp_id):
        if self.rc.exists("statistic:{}".format(str(sp_id))):
            self.rc.delete("statistic:{}".format(str(sp_id)))
            print("删除redis键：{}".format("statistic:{}".format(str(sp_id))))
# profit_contri_customer



def delete():
    try:
        MongoCache().delete_salesman_ticket_trend_cache().delete_salesman_rank_cache().delete_goods_sale_trend_cache().\
        delete_goods_sale_rank_cache().delete_shop_sale_record_cache()

        # RedisCache().delete_tj(572)
    except Exception as e:
        print("未知错误，可能删除没成功")
        raise e
    print("后台/数据中心 缓存删除成功")
    RedisCache().delete_tj(425)

if __name__ == '__main__':
    delete()

