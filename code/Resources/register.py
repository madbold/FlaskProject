
from flask import Flask,request
from flask_restful import Resource,Api
import sqlite3
from Model.usr import UserModel
class UserRegister(Resource):
    def post(self):

        data= request.get_json()
        userObj=UserModel(None,data["username"],data["password"])
        userObj.save_to_db()
        return {"Message":"User successfully added"}
