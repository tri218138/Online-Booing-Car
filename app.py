from flask import Flask, render_template, request, jsonify, get_template_attribute, make_response, redirect, url_for
import numpy as np
from python.DBMS import Cursor, Database
from python.person import Person
import json

class TemplateHTML:
    def __init__(self):
        self.role = ''
    def setRole(self, role_):
        self.role = role_
        self.setHeaderHTML()
    def setHeaderHTML(self):
        self.headerHTML = render_template('header.html', role=self.role)
    def setOrderHTML(self, data_):
        self.orderHTML = render_template('order.html', role=self.role, data=data_)

person = Person()
templates = TemplateHTML()

def get_login_status():
    if not Person.defined():
        return False
    else:
        return True

def check_login(un, ps):
    if un == 'admin' and ps == 'admin':
        return True, 'admin0', 'admin'
    else:
        return True, 'user1', 'user'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if not person.defined():
        return redirect("/signin", code=302)
    else:
        demo = f'''
            <img id="demo-img-car" src="{url_for('static', filename='img/certificate/BMW-cover-edit-8070-1567150808.jpg')}"
                class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
        '''
        if person.getRole() == 'admin':
            # headerHTML = render_template('header.html', role='admin')
            return render_template('index.html', header=templates.headerHTML, gallery = demo)
        else:
            # headerHTML = render_template('header.html')
            return render_template('index.html', header=templates.headerHTML, gallery = demo)

@app.route('/signin', methods=['GET','POST'])
def signin():
    if not person.defined():
        if request.method == 'POST':
            un = request.form['username']
            ps = request.form['password']
            res, personID, role = check_login(un, ps)
            if res:
                person.definePerson(personID, role)
                templates.setRole(role)
                return redirect('/', code=302)
            else:
                # abort(401)
                print('failure')
                signin = render_template('signin.html', failure=True)
                return render_template('index.html', signin = signin)
        else:
            signin = render_template('signin.html')
            return render_template('index.html', signin = signin)
    else:
        return redirect("/", code=302)

@app.route('/model', methods=['GET','POST'])
def model():
    if not person.defined():
        return redirect("/signin", code=302)
    Cursor.execute("SELECT model_urlImage, model_name, model_description FROM onlinebookingcar.car")
    data = Cursor.fetchall()
    modelGallery = render_template('model.html', data = data)
    return render_template('index.html', header=templates.headerHTML, gallery=modelGallery)

@app.route('/build', methods=['GET','POST'])
def build():
    if not person.defined():
        return redirect("/signin", code=302)
    if request.method == "POST":
        form = request.form.to_dict()
        form = json.dumps(form)
        Cursor.execute(f"INSERT INTO onlinebookingcar.orderList (components) VALUES ('{form}')")
        Database.commit()
        return redirect("/build", code=302)
    if request.method == "GET":
        navBarBuild = render_template('build/navbar.html')
        demo = '''
            <img id="demo-img-car" src="http://drive.google.com/uc?export=view&id=1Z2gn9zjGLk599lp8QKKiP4gO1Q724uI8"
                class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
        '''
        data = {}
        Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'design'")
        data["design"] = Cursor.fetchall()
        Cursor.execute("SELECT id,component_name,component_description,urlImage FROM onlinebookingcar.component WHERE component_type = 'interior'")
        data["interior"] = Cursor.fetchall()
        tmp = render_template('/build/sidebar.html', data=data)
        return render_template('index.html', header=templates.headerHTML, content=demo, navBarBuild = navBarBuild, sidebar=tmp)
@app.route('/summary', methods=['GET','POST'])
def summary():
    return render_template('index.html', header=templates.headerHTML)

@app.route('/order', methods=['GET'])
def orderPage():
    if not person.defined():
        return redirect("/signin", code=302)
    # ##############################
    if person.getRole() == 'admin':
        Cursor.execute("SELECT * FROM orderList")
        dataList = Cursor.fetchall()
        for rec in dataList:
            rec["components"] = json.loads(rec["components"])
            for field in ["design", "exterior", "interior"]:
                if field in rec["components"]:
                    rec[field] = rec["components"][field]

        # dataOrderList = [{
        #     'orderID': 'SOFA1XQ',
        #     'userId': 'user0',
        #     'design': 'design1',
        #     'exterior' : 'exterior2',
        #     'interior' : 'interior1',
        #     'orderTime' : '15/12/2022'
        # }]
        templates.setOrderHTML(dataList)
        return render_template('index.html', header=templates.headerHTML, order = templates.orderHTML)
    else:
        dataOrderList = [{
            'orderID': 'SOFA1XQ',
            'design': 'design1',
            'exterior' : 'exterior2',
            'interior' : 'interior1',
            'orderTime' : '15/12/2022'
        }]
        templates.setOrderHTML(dataOrderList)
        return render_template('index.html', header=templates.headerHTML, order = templates.orderHTML)

@app.route('/logout', methods=['GET'])
def logout():
    if not person.defined():
        return redirect("/signin", code=302)
    else:
        person.quit()
        return redirect('/', 302)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/', 302)


if __name__ == "__main__":
    app.run(debug=True)

# ref: https://ourtechroom.com/tech/use-google-drive-image-in-html-and-website/