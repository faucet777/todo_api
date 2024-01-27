import pymongo


host = 'localhost'
port = 27111
collection_todo = pymongo.MongoClient(host, port)['todo_db']['todo_collection']


