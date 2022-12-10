import pymysql.cursors
import json
import itertools
import bcrypt


Database = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="BWM",
    cursorclass=pymysql.cursors.DictCursor
)
Cursor = Database.cursor()

class DBMS:
    def __init__(self):
        self.Database = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="BWM",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.Cursor = self.Database.cursor()
    def store(self):
        self.Database.commit()
        
    # Log in sign up 
    
    # def checkSignin(self, username, password):
    #     password  = password.encode('utf-8')
    #     sql ="SELECT username, password FROM CusAccount WHERE username = %s"
    #     Cursor.execute(sql, username)
    #     cus = Cursor.fetchall()
    #     if (len(cus) == 1):
    #         cus = cus[0]
    #         if bcrypt.checkpw(password,cus["password"].encode('utf-8')):
    #             return username, "customer"
    #         else :
    #             raise Exception("Invalid password or username")
    #     sql ="SELECT username, password,typejob FROM Account A , Employee E WHERE username = %s AND A.empID = E.id"
    #     Cursor.execute(sql, username)
    #     cus = Cursor.fetchall()        
    #     if (len(cus) == 1):
    #         cus = cus[0]
    #         if bcrypt.checkpw(password, cus["password"].encode('utf-8')):
    #             return username,  cus["typejob"].lower()
    #         else :
    #             raise Exception("Invalid password or username")           
    #     raise Exception("Username does not exist")           

        
    def signUpCustomer(self, username, password, address, phonenumber, name, BA_ID):
        # generating the salt
        salt = bcrypt.gensalt()
        bytes = password.encode('utf-8')
        password = bcrypt.hashpw(bytes, salt).decode('utf-8')
        sql = "SELECT username FROM Account WHERE username = %s UNION SELECT username FROM CusAccount WHERE username = %s"
        Cursor.execute(sql, (username, username))
        existedAccount = Cursor.fetchall()       
        print(existedAccount)
        if (len(existedAccount) != 0):
            raise Exception("This username has been used!") 
        sql = "INSERT INTO Customer(address,phonenumber,name, BA_ID) VALUES(%s,%s,%s,1)"
        Cursor.execute(sql, (address, phonenumber,name))
        Database.commit()
        newCusID = Cursor.lastrowid
        sql = "INSERT INTO CusAccount(username, password, cusID) VALUES(%s,%s,%s)"
        Cursor.execute(sql, (username, password ,newCusID))
        Database.commit()
        return username, "customer"      
    
      
    # END log in sign up
    
    # def getDemoImage(self):
    #     return f'''
    #         <img id="demo-img-car" src="https://www.bmw.vn/content/dam/bmw/common/all-models/3-series/sedan/2018/inspire/bmw-3series-3er-inspire-sp-xxl.jpg.asset.1627477249501.jpg"
    #             class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
    #     '''
    # def getModelsDetail(self, role):
    #     if role == 'admin':
    #         Cursor.execute("SELECT id, model_urlImage, model_name, model_description FROM onlinebookingcar.car")
    #         return Cursor.fetchall()
    #     elif role == 'user':
    #         Cursor.execute("SELECT model_urlImage, model_name, model_description FROM onlinebookingcar.car")
    #         return Cursor.fetchall()
    # def updateModelDetail(self, model_id, data):
    #     Cursor.execute(f"UPDATE onlinebookingcar.car \
    #                 SET model_urlImage = '{data['model_urlImage']}',\
    #                     model_name = '{data['model_name']}',\
    #                     model_description = '{data['model_description']}'\
    #                 WHERE id = '{data['id']}';")
    # def addOrder(self, data):
    #     Cursor.execute(f"INSERT INTO onlinebookingcar.orderList (components) VALUES ('{data}')")
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
    
    def getModelByID(self, id):
        self.Cursor.execute("SELECT * FROM bwm.car WHERE id = %s",(id))
        data = self.Cursor.fetchall()
        return data[0]
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