from peewee import *

database = SqliteDatabase("database.sqlite")

class BaseModel(Model):
    class Meta:
        database = database


class AccountModel(BaseModel):
    username = CharField(max_length=64)

    password = TextField(default="")

    salt = TextField(default="")    
    data = TextField(default="")
    nonce = TextField(default="")


class BlobModel(BaseModel):
    bid = TextField()
    data = TextField(default="")


