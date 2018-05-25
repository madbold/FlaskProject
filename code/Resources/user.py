
from flask import Flask,request
from flask_restful import Resource,Api
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required ,get_jwt_claims,get_jwt_identity,jwt_refresh_token_required
from flask_jwt_extended import create_access_token ,create_refresh_token ,get_raw_jwt
from blacklist import BLACKLIST
from Model.usr import UserModel
class User(Resource):
    def get(self,user_id):

        userObj= UserModel.find_user_by_id(user_id)
        if userObj:
            return userObj.json()
        return {"Message":"User not found"}

    @jwt_required
    def delete(self,user_id):
        claims= get_jwt_claims()
        if not claims["is_admin"]:
            return {"msg":"You are not authorized to delelte item. contact admin"}
        userObj= UserModel.find_user_by_id(user_id)
        if userObj:
            userObj.delete_from_db()
            return {"Message":"User delete"}

        return {"Message":"User not found to delete"}

class UserLogin(Resource):

    def post(self):
        data= request.get_json()
        user=UserModel.find_user_by_name(data["username"])
        if user and safe_str_cmp(user.password,data["password"]):
            access_token=create_access_token(identity=user.id,fresh=True)
            refresh_token= create_refresh_token(user.id)
            return{
                   "access_token": access_token ,
                   "refresh_token" :refresh_token
                   }

        return {"msg": "invalid credential!"},401

class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user=get_jwt_identity()
        new_token=create_access_token(identity=current_user,fresh=False)
        return {'access_token':new_token}

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti= get_raw_jwt() # jti is unique identifier for access token
        BLACKLIST.add(jti['jti'])
