from flask import Blueprint, request, Response, render_template, session, redirect, url_for
from model.dbms import dbms
from controller.main import TOKEN, defineToken
import json

customer_bp = Blueprint('customer_bp', __name__, template_folder="./views")

@customer_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign or auth["role"] != 'customer':
        return redirect(url_for('main_bp.login'))

@customer_bp.route('/', methods=['GET', 'POST'])
@customer_bp.route('/home', methods=['GET', 'POST'])
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

@customer_bp.route('/model', methods=['GET', 'POST'])
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
# @customer_bp.route('/model/detail', methods=['GET', 'POST'])
# def modelDetail():
#     data = {}
#     if request.method == 'GET':
#         req = request.args.to_dict()
#         if "id" in req:
#             data["car"] = dbms.selectModelById(req["id"]) #use later
#             # data["car"] = dbms.selectModelById('1')
#         if "angle" in req:
#             data["car"]["img_url"] = re.sub("&angle=.{2}&|&angle=.{3}&|&angle=.{1}&", f"&angle={req['angle']}&", data["car"]["img_url"])
#             # print(data)
#     header = render_template('component/header.html')
#     footer = render_template('component/footer.html')
#     detail = render_template('component/detail.html', data= data)
#     content = render_template('layout/2.html', header=header, content=detail, footer=footer)
#     return render_template('index.html', content=content)

@customer_bp.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        data = json.loads(request.data)
        # add database bill
        return Response('BMW cảm ơn bạn đã đồng hành', 200)
    else:
        args = request.args.to_dict()
        if len(args.values()) == 1:
            args["type"] = 'Exterior'
            args["subtype"] = 'Color'
        data = {}
        if args["type"] != 'Summary':
            data = {
                "component": dbms.getListComponent(int(args['id']), args["type"], args["subtype"]),
                "url": dbms.getURLCar(int(args['id'])).replace('&angle=40&','&angle=90&'),
                "type": args["type"],
                "subtype": args["subtype"]
            }
        else:
            item = ['Color', 'Wheel', 'Upholstery', 'Trim']
            items = []
            for i in item:
                if i in args.keys():
                    items.append(dbms.getPriceByName(args["Color"], i))
            data = {
                "component": [],
                "url": dbms.getURLCar(int(args['id'])).replace('&angle=40&','&angle=90&'),
                "type": args["type"],
                "subtype": args["subtype"],
                "items": items
            }
        print(data)
        header = render_template('component/header.html')
        build = render_template('component/build.html', data= data)
        content = render_template('layout/2.html', header=header, content=build)
        return render_template('index.html', content=content)

@customer_bp.route('/profile', methods=['GET', 'POST'])
def personalInfomation():
    data = {}
    data["customer"] = dbms.selectCustomerById(auth["id"])
    data["mode"] = 'view'
    if request.method == "GET":
        req = request.args.to_dict()
        if "mode" in req:
            if req["mode"] == "edit":
                data["mode"] = "edit"
    elif request.method == "POST":
        req = request.form.to_dict() #{'name': 'Juana Bonhomme', 'email': '', 'phone': '+86-222-233-47688', 'address': '44 Riverside Street', 'request': 'save'}
        if req["request"] == "save":
            dbms.saveCustomerProfile(auth["id"], data=req)
            return redirect(url_for("customer_bp.personalInfomation"))
        elif req["request"] == "cancel":
            return redirect(url_for("customer_bp.personalInfomation"))
    container = render_template('component/profile.html', data=data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    content = render_template('layout/2.html', header=header, content=container, footer=footer)
    return render_template('index.html', content=content)

@customer_bp.route('/setting', methods=['GET', 'POST'])
def personalSetting():
    data = {}
    container = render_template('pages/setting.html', data=data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    content = render_template('layout/2.html', header=header, content=container, footer=footer)
    return render_template('index.html', content=content)

@customer_bp.route('/model/detail', methods=['GET', 'POST'])
def detail():
    carID = request.args['id']
    car = dbms.getModelByID(carID)
    faq= dbms.getfaq(carID)
    data = {
        "car": car,
        "faq": faq
    }
    if request.method == 'GET':
        req = request.args.to_dict()
        if "angle" in req:
            data["car"]["img_url"] = re.sub("&angle=.{2}&|&angle=.{3}&|&angle=.{1}&", f"&angle={req['angle']}&", data["car"]["img_url"])
    header = render_template('component/header.html')
    model = render_template('component/detail.html', data= data)
    content = render_template('layout/1.html', header=header, content=model)
    return render_template('index.html', content=content)


@customer_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('customer_bp.home'))
