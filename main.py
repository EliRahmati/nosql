import pymongo
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('localhost', 27017, username='elhamrahmati', password='e3r4t5')
db = client.social_media_db

# Define collections
users_collection = db.users
posts_collection = db.posts
followers_collection = db.followers
likes_collection = db.likes
comments_collection = db.comments

users_collection.create_index([("user_id", pymongo.ASCENDING)], unique=True)
posts_collection.create_index([("post_id", pymongo.ASCENDING)], unique=True)
followers_collection.create_index([("follower_id", pymongo.ASCENDING)], unique=True)
likes_collection.create_index([("like_id", pymongo.ASCENDING)], unique=True)
comments_collection.create_index([("comment_id", pymongo.ASCENDING)], unique=True)

# Sample data
users_data = [
    {"user_id": 1, "username": "user1", "email": "user1@example.com", "password_hash": "hashed_password1", "bio": "User 1's bio", "profile_picture_url": "http://example.com/user1.jpg", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"user_id": 2, "username": "user2", "email": "user2@example.com", "password_hash": "hashed_password2", "bio": "User 2's bio", "profile_picture_url": "http://example.com/user2.jpg", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    # Add more users as needed
]

posts_data = [
    {"post_id": 1, "user_id": 1, "content": "This is a post by user 1", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"post_id": 2, "user_id": 2, "content": "This is a post by user 2", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    # Add more posts as needed
]

followers_data = [
    {"user_id": 2, "follower_id": 1},
    # Add more follower relationships as needed
]

likes_data = [
    {"like_id": 1, "post_id": 1, "user_id": 2},
    # Add more likes as needed
]

comments_data = [
    {"comment_id": 1, "post_id": 1, "user_id": 2, "content": "Nice post!", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    # Add more comments as needed
]

# Insert sample data into collections
users_collection.insert_many(users_data)
posts_collection.insert_many(posts_data)
followers_collection.insert_many(followers_data)
likes_collection.insert_many(likes_data)
comments_collection.insert_many(comments_data)

print("Sample data inserted successfully.")
