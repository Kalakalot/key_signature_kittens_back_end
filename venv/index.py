import pymongo
import config

my_client = pymongo.MongoClient(config.MONGO_URI)

try:
    print("MongoDB version is %s" %
            my_client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)