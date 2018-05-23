from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import jwt_required
from Model.items import ItemModel

class Item(Resource):
    @jwt_required()
    def get(self,name):

        item=ItemModel.getItembyName(name)
        if item:
            return item.json()
        return{"MSG":"Item {0} not found".format(name)}

    def post(self,name):

        item=ItemModel.getItembyName(name)
        if item:
            return {"msg":"Item with name {0} already exist".format(name)}

        data= request.get_json()
        item=ItemModel(name,data["price"],data["store_id"])
        new_item,code = item.AddItem()
        return new_item,code

    def put(self,name):

        data= request.get_json()
        item=ItemModel.getItembyName(name)
        if item:
            item.price=data["price"]
            item.store_id=data["store_id"]
        else:
            item=ItemModel(name,data["price"],data["store_id"])
        return item.AddItem()


    def delete(self,name):
        item=ItemModel.getItembyName(name)
        if item:
            item.delete_from_db()
            return {"msg":"Deleted {0}".format(name)}, 200

        return {"msg":"Item not found to delete"},200

class ItemList(Resource):
    def get(self):
        itemlist= ItemModel.getallItems()
        return [item.json() for item in itemlist ]
