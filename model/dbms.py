import pymysql.cursors
import json
import itertools
# from model.database import *

class DBMS:
    def __init__(self):
        self.Database = pymysql.connect(
            host="localhost",
            user="root",
            password="280818",
            database="bwm",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.Cursor = self.Database.cursor()
    def store(self):
        self.Database.commit()
    def checkSignin(self, un, ps):
        self.Cursor.execute(f"SELECT * FROM bwm.cusaccount WHERE username = '{un}' AND password = '{ps}'" )
        data = self.Cursor.fetchone() # {}
        if len(data) > 0:
            return {"status": True, "id": data["cusID"], "role": "customer"}
        else:
            self.Cursor.execute(f"SELECT * FROM bwm.account WHERE username = '{un}' AND password = '{ps}'" )
            data = self.Cursor.fetchone() # {}
            if len(data) > 0:
                empID = data["empID"]
                self.Cursor.execute(f"SELECT * FROM bwm.employee WHERE id = '{empID}'" )
                data = self.Cursor.fetchone() # {}
                role = data["typejob"].lower()
                return {"status": True, "id": data["empID"], "role": role}
            else:
                return {"status": False}
    def getModelsDetail(self):
        self.Cursor.execute("SELECT * FROM bwm.car")
        data = self.Cursor.fetchall()
        return data
    def selectComponentByType(self, type):
        self.Cursor.execute(f"SELECT * FROM bwm.component WHERE type = '{type}'")
        data = self.Cursor.fetchall()
        for d in data:
            d["description"] = d["desciption"]
        return data
    def selectComponentById(self, id):
        self.Cursor.execute(f"SELECT * FROM bwm.component WHERE id = '{id}'")
        data = self.Cursor.fetchone()
        data["description"] = data["desciption"]
        return data
    # def getDemoImage(self):
    #     return f'''
    #         <img id="demo-img-car" src="https://www.bmw.vn/content/dam/bmw/common/all-models/3-series/sedan/2018/inspire/bmw-3series-3er-inspire-sp-xxl.jpg.asset.1627477249501.jpg"
    #             class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
    #     '''
    # def updateModelDetail(self, model_id, data):
    #     self.Cursor.execute(f"UPDATE onlinebookingcar.car \
    #                 SET model_urlImage = '{data['model_urlImage']}',\
    #                     model_name = '{data['model_name']}',\
    #                     model_description = '{data['model_description']}'\
    #                 WHERE id = '{data['id']}';")
    # def addOrder(self, data):
    #     self.Cursor.execute(f"INSERT INTO onlinebookingcar.orderList (components) VALUES ('{data}')")

    # def getDesignComponent(self):
    #     self.Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'design'")
    #     return self.Cursor.fetchall()
    # def getInteriorComponent(self):
    #     self.Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'interior'")
    #     return self.Cursor.fetchall()
    # def getOrderList(self, role):
    #     if role == 'user':
    #         dataOrderList = [{
    #             'orderID': 'SOFA1XQ',
    #             'design': 'design1',
    #             'exterior' : 'exterior2',
    #             'interior' : 'interior1',
    #             'orderTime' : '15/12/2022'
    #         }]
    #         return dataOrderList
    #     else:
    #         self.Cursor.execute("SELECT * FROM orderList")
    #         return self.Cursor.fetchall()
    # def removeOrder(self, data_):
    #     self.Cursor.execute(f"DELETE FROM onlinebookingcar.orderList WHERE orderID = '{data_['orderID']}'")
        
dbms = DBMS()

# $12$YsUHM2Huyh6.v09SMRIqJOhQc9P9YFIh8g8xDqvjfx0FUghxaR33S