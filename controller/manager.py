from flask import Blueprint, request, render_template, session, redirect, url_for
from model.dbms import dbms
from controller.main import TOKEN, defineToken

manager_bp = Blueprint('manager_bp', __name__, template_folder="./views")

@manager_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign:
        return redirect(url_for('main_bp.login'))

@manager_bp.route('/', methods=['GET', 'POST'])
@manager_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    data = {
        "top": dbms.selectTopKModel(4, 'year')
    }
    # print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    home = render_template('pages/home.html', data=data)
    content = render_template('layout/3.html', header=header, content=home, footer=footer)
    return render_template('index.html', content=content)

@manager_bp.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'GET':
        req = request.args.to_dict()
        if "type" in req:
            type = req["type"]
            data = {
                "models": dbms.getModelsDetailByType(type) #[]
            }
            # print(data)
            header = render_template('component/header.html')
            footer = render_template('component/footer.html')
            model = render_template('component/model.html', data= data)
            content = render_template('layout/1.html', header=header, content=model, footer=footer)
            return render_template('index.html', content=content)
    data = {
        "models": dbms.getModelsDetail() #[]
    }
    # print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    model = render_template('component/model.html', data= data)
    content = render_template('layout/1.html', header=header, content=model, footer=footer)
    return render_template('index.html', content=content)

import re
@manager_bp.route('/model/detail', methods=['GET', 'POST'])
def detail():
    data = {}
    if request.method == 'GET':
        req = request.args.to_dict()
        if "id" in req:
            data["car"] = dbms.selectModelById(req["id"]) #use later
            # data["car"] = dbms.selectModelById('1')
        if "angle" in req:
            data["car"]["img_url"] = re.sub("&angle=.{2}&|&angle=.{3}&|&angle=.{1}&", f"&angle={req['angle']}&", data["car"]["img_url"])
            # print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    detail = render_template('component/detail.html', data= data)
    content = render_template('layout/2.html', header=header, content=detail, footer=footer)
    return render_template('index.html', content=content)

@manager_bp.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        req = request.args.to_dict()
        # print(req)
    data = {}
    # print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    build = render_template('component/build.html', data= data)
    content = render_template('layout/2.html', header=header, content=build, footer=footer)
    return render_template('index.html', content=content)

@manager_bp.route('/project', methods=['GET', 'POST'])
def project():
    header = render_template('component/header.html')
    if request.method == 'POST':
        req = request.form.to_dict()
        if "profectId" in req:
            data_ = {
                "id": req["profectId"],
                "progress" : req["progress"],
            }
            dbms.updateProjectProgress(data_)
    # content = """<h1>Trang mà leader nhận các đơn đặt ô tô của khách hàng, sau đó khởi động cho manager quản lý</h1>"""
    data = {
        "myproject": dbms.selectBusinessProjects()
    }
    content = render_template('pages/myproject.html',data=data)
    content = render_template('layout/1.html', header=header, content = content)
    return render_template('index.html', content=content)

@manager_bp.route('/profile', methods=['GET', 'POST'])
def personalInfomation():
    data = {}
    data["customer"] = dbms.selectCustomerById(auth["idlogin"])
    data["mode"] = 'view'
    if request.method == "GET":
        req = request.args.to_dict()
        if "mode" in req:
            if req["mode"] == "edit":
                data["mode"] = "edit"
    elif request.method == "POST":
        req = request.form.to_dict() #{'name': 'Juana Bonhomme', 'email': '', 'phone': '+86-222-233-47688', 'address': '44 Riverside Street', 'request': 'save'}
        if req["request"] == "save":
            dbms.saveCustomerProfile(auth["idlogin"], data=req)
            return redirect(url_for("manager_bp.personalInfomation"))
        elif req["request"] == "cancel":
            return redirect(url_for("manager_bp.personalInfomation"))
    container = render_template('component/profile.html', data=data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    content = render_template('layout/2.html', header=header, content=container, footer=footer)
    return render_template('index.html', content=content)

@manager_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('manager_bp.home'))
