from flask_mongoengine  import MongoEngine

url="mongodb+srv://sam:1234@cluster0.eemjyoy.mongodb.net/Annamalai?retryWrites=true&w=majority"



mydb=MongoEngine()
class Laptop(mydb.Document):
    model=mydb.StringField()
    serial=mydb.StringField()
    ram=mydb.IntField()
    ssd=mydb.IntField()
    stock=mydb.IntField()
    price=mydb.IntField()
    type=mydb.StringField()



