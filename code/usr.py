import sqlite3
from db import db
class UserModel(db.Model):

    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(40))

    def __init__(self,username,password):

        self.username=username
        self.password=password


    def json(self):
        return {"name": self.username}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_user_by_name(cls,name):
        return cls.query.filter_by(username=name).first()


    @classmethod
    def find_user_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
