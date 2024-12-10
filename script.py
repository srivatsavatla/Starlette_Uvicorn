""" 
Script to parse course information from courses.json, create the appropriate databases and
collection(s) on a local instance of MongoDB, create the appropriate indices (for efficient retrieval)
and finally add the course data on the collection(s).
"""

import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://srivatsav:srivatsav@cluster0.0pmprnp.mongodb.net/")
db = client["Courses"]
collection = db["courses"]

with open("courses.json", "r") as f:
    courses = json.load(f)

collection.create_index("name")

for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

for course in courses:
    collection.insert_one(course)

client.close()