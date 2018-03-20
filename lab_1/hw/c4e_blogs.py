from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    "title" : "Tuyên ngôn... l4d2",
    "author" : "game thủ",
    "content" : """Tất cả mọi người sinh ra đều có quyền bình đẳng.
    Tạo hóa cho họ những quyền không ai có thể xâm phạm được, trong những quyền ấy,
    có quyền được charger đâm,
    quyền tự do được smoker đá lưỡi,
    quyền được cõng jockey,
    quyền được hunter theo đuổi,
    và quyền được witch âu yếm."""
}

posts.insert_one(new_post)
