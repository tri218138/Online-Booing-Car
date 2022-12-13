import pymysql.cursors
import json
import itertools
import bcrypt

class DBMS:
    def __init__(self):
        self.Database = pymysql.connect(
            host="localhost",
            user="root",
            password="280818",
            database="bmw",
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
        self.Cursor.execute(sql, (username, username))
        existedAccount = self.Cursor.fetchall()       
        print(existedAccount)
        if (len(existedAccount) != 0):
            raise Exception("This username has been used!") 
        sql = "INSERT INTO Customer(address,phonenumber,name, BA_ID) VALUES(%s,%s,%s,1)"
        self.Cursor.execute(sql, (address, phonenumber,name))
        self.Database.commit()
        newCusID = self.Cursor.lastrowid
        sql = "INSERT INTO CusAccount(username, password, cusID) VALUES(%s,%s,%s)"
        self.Cursor.execute(sql, (username, password ,newCusID))
        self.Database.commit()
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
        self.Cursor.execute(f"SELECT * FROM bmw.cusaccount WHERE username = '{un}' AND password = '{ps}'" )
        data = self.Cursor.fetchone() # {}
        if data is not None:
            return {"status": True, "id": data["cusID"], "role": "customer"}
        else:
            self.Cursor.execute(f"SELECT * FROM bmw.account WHERE username = '{un}' AND password = '{ps}'" )
            data = self.Cursor.fetchone() # {}
            if data is not None:
                empID = data["empID"]
                self.Cursor.execute(f"SELECT * FROM bmw.employee WHERE id = '{empID}'" )
                data = self.Cursor.fetchone() # {}
                role = data["typejob"].lower()
                return {"status": True, "id": empID, "role": role}
            else:
                return {"status": False}
    def getModelsDetail(self):
        self.Cursor.execute(f"SELECT * FROM bmw.car")
        data = self.Cursor.fetchall()
        return data
    def getModelsDetailByType(self, type):
        self.Cursor.execute(f"SELECT * FROM bmw.car WHERE series_name LIKE '%{type}%'")
        data = self.Cursor.fetchall()
        return data
    def selectComponentByType(self, type):
        self.Cursor.execute(f"SELECT * FROM bmw.component WHERE type = '{type}'")
        data = self.Cursor.fetchall()
        for d in data:
            d["description"] = d["desciption"]
        return data
    def selectComponentById(self, id):
        self.Cursor.execute(f"SELECT * FROM bmw.component WHERE id = '{id}'")
        data = self.Cursor.fetchone()
        data["description"] = data["desciption"]
        return data
    def selectModelById(self, id):
        self.Cursor.execute(f"SELECT * FROM bmw.car WHERE id = '{id}'")
        data = self.Cursor.fetchone()
        return data
    def selectCustomerById(self, id):
        self.Cursor.execute(f"SELECT * FROM bmw.customer WHERE id = '{id}'")
        data = self.Cursor.fetchone()
        data["phone"] = data["phonenumber"]
        return data
    def selectEmployeeById(self, id):
        self.Cursor.execute(f"SELECT * FROM bmw.employee WHERE id = '{id}'")
        data = self.Cursor.fetchone()
        #{'id': 4, 'Name': 'Eployee 4', 'salary': 1500.0, 'SSN': 1000003, 'typejob': 'Manager', 'languageSkill': 'good', 'technicalSkill': 'good', 'manageSkill': 'good', 'memID': None}
        data["name"] = data["Name"]
        # print(data)
        return data

    def selectTopKModel(self, k, attr):
        if attr == 'year':
            self.Cursor.execute(f"SELECT * FROM bmw.car ORDER BY year DESC LIMIT 4")
            data = self.Cursor.fetchall()
            return data

    def saveCustomerProfile(self, id, data):
        self.Cursor.execute(f"UPDATE bmw.customer SET \
                name = '{data['name']}' , \
                address = '{data['address']}' ,\
                phonenumber = '{data['phone']}' \
                WHERE id = '{id}'\
            ")
        self.Database.commit()
    def saveEmployeeProfile(self, id, data):
        self.Cursor.execute(f"UPDATE bmw.employee SET \
                name = '{data['name']}' , \
                address = '{data['address']}' ,\
                phonenumber = '{data['phone']}' \
                WHERE id = '{id}'\
            ")
        self.Database.commit()

    def selectBusinessOrders(self):
        self.Cursor.execute(f"SELECT * FROM bmw.order")
        data = self.Cursor.fetchall()
        return data
    def selectBusinessProjects(self):
        self.Cursor.execute(f"SELECT * FROM bmw.project")
        data = self.Cursor.fetchall()
        return data

    def updateProjectProgress(self, data):
        self.Cursor.execute(f"UPDATE bmw.project SET progress = '{data['progress']}' WHERE id = '{data['id']}'")
        self.Database.commit()
    def getListComponent(self, id, type, subtype):
        if subtype != "Summry":
            type = type.lower()
            subtype = subtype.lower()
            self.Cursor.execute(f"SELECT name FROM ((SELECT * FROM bmw.component WHERE type = '{type}' AND carID = {id}) as a JOIN bmw.{type} ON a.id = {type}ID) WHERE {type}Type = '{subtype}'")
            data = self.Cursor.fetchall()
            return data
        else:
            return {}
    
    def getURLCar(self, id):
        self.Cursor.execute(f"SELECT img_url FROM bmw.car WHERE id = {id}")
        data = self.Cursor.fetchall()
        return data[0]['img_url']

    def getPriceByName(self, name, type):
        self.Cursor.execute(f"SELECT name, price FROM bmw.component WHERE type = '{type}' AND name = '{name}'")
        data = self.Cursor.fetchall()
        return data[0]

    
    def getModelByID(self, id):
        self.Cursor.execute("SELECT * FROM bmw.car WHERE id = %s",(id))
        data = self.Cursor.fetchall()
        return data[0]
    
    def getfaq(self, carid):
        self.Cursor.execute("SELECT * FROM bmw.faq WHERE carid = %s",(carid))
        data = self.Cursor.fetchall()
        return data
    
    def updateCar(self, carid, data):
        updateData = (data["model_name"],data["series_name"],data["title"],data["branch"],data["mass"],data["starting_msrp"],data["year"], carid)
        try: 
            self.Cursor.execute("UPDATE car SET model_name = %s, series_name = %s, title = %s, branch = %s, mass = %s, starting_msrp = %s, year = %s WHERE id = %s",updateData)
            self.Database.commit()           
        except (pymysql.Error) as e:
            return e

        return ""
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