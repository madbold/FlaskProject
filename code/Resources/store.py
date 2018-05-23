from flask_restful import Resource
from Model.store import StoreModel
from flask import Flask,request

class Store(Resource):

    def get(self,name):
        store=StoreModel.getItembyName(name)
        if store:
            return store.json()
        return{"msg":"Store not found"},404

    def post(self,name):
        store=StoreModel.getItembyName(name)
        if store:
            return {"msg":"Store {0} already exist".format(name)}


        store=StoreModel(name)
        store.AddItem()


    def delete(self,name):
        store=StoreModel.getItembyName(name)
        if not store:
            return {"msg":"unbale to deleted. {0}: store not found".format(name)}
        store.delete_from_db()

class StoreList(Resource):
    def get(self):
        stores=StoreModel.getallItems()
        return [ store.json() for store in stores]
