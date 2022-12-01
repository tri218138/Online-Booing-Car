import pymysql.cursors
import json
import itertools

from model.database import *

Database = pymysql.connect(
    host="localhost",
    user="root",
    password="280818",
    database="onlinebookingcar",
    cursorclass=pymysql.cursors.DictCursor
)
Cursor = Database.cursor()

class DBMS:
    def __init__(self):
        self.Database = pymysql.connect(
            host="localhost",
            user="root",
            password="280818",
            database="onlinebookingcar",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.Cursor = self.Database.cursor()
    def store(self):
        self.Database.commit()
    def checkSignin(self, un, ps):
        if un == 'admin' and ps == 'admin':
            return True, 'admin0', 'admin'
        else:
            return True, 'user1', 'user'
    def getDemoImage(self):
        return f'''
            <img id="demo-img-car" src="https://www.bmw.vn/content/dam/bmw/common/all-models/3-series/sedan/2018/inspire/bmw-3series-3er-inspire-sp-xxl.jpg.asset.1627477249501.jpg"
                class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
        '''
    def getModelsDetail(self, role):
        if role == 'admin':
            Cursor.execute("SELECT id, model_urlImage, model_name, model_description FROM onlinebookingcar.car")
            return Cursor.fetchall()
        elif role == 'user':
            Cursor.execute("SELECT model_urlImage, model_name, model_description FROM onlinebookingcar.car")
            return Cursor.fetchall()
    def updateModelDetail(self, model_id, data):
        Cursor.execute(f"UPDATE onlinebookingcar.car \
                    SET model_urlImage = '{data['model_urlImage']}',\
                        model_name = '{data['model_name']}',\
                        model_description = '{data['model_description']}'\
                    WHERE id = '{data['id']}';")
    def addOrder(self, data):
        Cursor.execute(f"INSERT INTO onlinebookingcar.orderList (components) VALUES ('{data}')")

    def getDesignComponent(self):
        Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'design'")
        return Cursor.fetchall()
    def getInteriorComponent(self):
        Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'interior'")
        return Cursor.fetchall()
    def getOrderList(self, role):
        if role == 'user':
            dataOrderList = [{
                'orderID': 'SOFA1XQ',
                'design': 'design1',
                'exterior' : 'exterior2',
                'interior' : 'interior1',
                'orderTime' : '15/12/2022'
            }]
            return dataOrderList
        else:
            Cursor.execute("SELECT * FROM orderList")
            return Cursor.fetchall()
    def removeOrder(self, data_):
        Cursor.execute(f"DELETE FROM onlinebookingcar.orderList WHERE orderID = '{data_['orderID']}'")
        
dbms = DBMS()