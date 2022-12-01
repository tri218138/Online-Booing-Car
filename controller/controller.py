from flask import request, jsonify, make_response, redirect, url_for
from app import app
from controller.person import person
from model.dbms import dbms
from view.view import view
import json

@app.route('/', methods=['GET','POST'])
def home():
    if not person.defined():
        return redirect("/signin", code=302)
    else:
        data = dbms.getDemoImage()
        if person.getRole() == 'admin':
            return view.render_template('/', data)
        else:
            return view.render_template('/', data)

@app.route('/signin', methods=['GET','POST'])
def signin():
    if not person.defined():
        if request.method == 'POST':
            un = request.form['username']
            ps = request.form['password']
            res, personID, role = dbms.checkSignin(un, ps)
            if res:
                person.definePerson(personID, role)
                view.setRole(role)
                return redirect('/', code=302)
            else:
                return view.render_template_signin(False)
        else:
            return view.render_template_signin(True)
    else:
        return redirect("/", code=302)

@app.route('/model', methods=['GET','POST'])
def model():
    if not person.defined():
        return redirect("/signin", code=302)
    if person.getRole() == 'admin':
        if request.method == 'POST':
            req = request.form.to_dict()
            if req["request"] == "update":
                dbms.updateModelDetail(req["id"], req)
    data = dbms.getModelsDetail(person.getRole())
    view.setModelGallery(data)
    return view.render_template('model')

@app.route('/build', methods=['GET','POST'])
def build():
    if not person.defined():
        return redirect("/signin", code=302)
    # if person.getRole() == 'admin':
    #     pass
    # elif person.getRole() == 'user':
    if request.method == "POST":
        req = request.form.to_dict()
        req = json.dumps(req)
        dbms.addOrder(req)
        return redirect("/build", code=302)
    if request.method == "GET":
        view.setNavBarBuild()
        data = {}            
        data["design"] = dbms.getDesignComponent()
        data["exterior"] = []
        data["interior"] = dbms.getInteriorComponent()
        view.setSideBarBuild(data)
    return view.render_template('build')

@app.route('/order', methods=['GET', 'POST'])
def orderPage():
    if not person.defined():
        return redirect("/signin", code=302)
    # ##############################
    if person.getRole() == 'admin':
        if request.method == "POST":
            req = request.form.to_dict()
            if req["request"] == "delete":
                dbms.removeOrder(req)
        
        dataOrderList = dbms.getOrderList(person.getRole())
        # rec = { "component" : {"design": "", "exterior": ,"interior":}}
        for rec in dataOrderList:
            rec["components"] = json.loads(rec["components"])
            for field in ["design", "exterior", "interior"]:
                if field in rec["components"]:
                    rec[field] = rec["components"][field]
        # rec = { "component" : {}, "design": {}, "exterior": {},"interior":{}}}
        view.setOrderHTML(dataOrderList)
    else:
        dataOrderList = dbms.getOrderList(person.getRole())    
        view.setOrderHTML(dataOrderList)
    return view.render_template('order')
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