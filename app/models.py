from datetime import datetime

from pymongo import MongoClient
from ming import Session, Field, schema, create_datastore
from ming.declarative import Document

session = Session(create_datastore('mongodb://localhost:27017/echo'))

db = MongoClient().echo


class Subscription(Document):
    class __mongometa__:
        session = session
        name = 'subscription'

    _id = Field(schema.ObjectId)
    url = Field(str)
    keyword = Field(str)
    synonyms = Field(str)
    mail = Field(str)
    offset = Field(datetime)


class Post(Document):
    class __mongometa__:
        session = session
        name = 'post'

    _id = Field(schema.ObjectId)
    created = Field(datetime)
    text = Field(str)
    page = Field(str)
    link = Field(str)
