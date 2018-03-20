from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds117729.mlab.com:17729/c4e16"


#1. connect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. creat collection
games = db['games']
blogs = db['blogs']


'''
#4.creat a new doc
new_game = {
    'name' : 'hung bia',
    'description' : 'best game ever'
}
new_blogs = {
    'title' : 'xac ban phim len va code',
    'content' : '.....'
}
#5. insert doc in collection
games.insert_one(new_game)
blogs.insert_one(new_blogs)
'''

all_game = games.find()

for game in all_game:
    print(game['name'])
