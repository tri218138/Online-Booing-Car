from flask import Blueprint, request, render_template, session, redirect, url_for
from model.dbms import dbms
from controller.main import TOKEN, defineToken

leader_bp = Blueprint('leader_bp', __name__, template_folder="./views")

@leader_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign:
        return redirect(url_for('main_bp.login'))

@leader_bp.route('/', methods=['GET', 'POST'])
@leader_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('component/project.html')
    content = render_template('layout/1.html', header=header,content=content)
    return render_template('index.html', content=content)

@leader_bp.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'GET':
        req = request.args.to_dict()
        if "type" in req:
            type = req["type"]
            data = {
                "models": dbms.getModelsDetailByType(type) #[]
            }
            print(data)
            header = render_template('component/header.html')
            footer = render_template('component/footer.html')
            model = render_template('component/model.html', data= data)
            content = render_template('layout/1.html', header=header, content=model, footer=footer)
            return render_template('index.html', content=content)
    data = {
        "models": dbms.getModelsDetail() #[]
    }
    print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    model = render_template('component/model.html', data= data)
    content = render_template('layout/1.html', header=header, content=model, footer=footer)
    return render_template('index.html', content=content)


import re
@leader_bp.route('/model/detail', methods=['GET', 'POST'])
def detail():
    data = {}
    if request.method == 'GET':
        req = request.args.to_dict()
        if "id" in req:
            data["car"] = dbms.selectModelById(req["id"]) #use later
            # data["car"] = dbms.selectModelById('1')
        if "angle" in req:
            data["car"]["img_url"] = re.sub("&angle=.{2}&|&angle=.{3}&|&angle=.{1}&", f"&angle={req['angle']}&", data["car"]["img_url"])
            print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    detail = render_template('component/detail.html', data= data)
    content = render_template('layout/2.html', header=header, content=detail, footer=footer)
    return render_template('index.html', content=content)

@leader_bp.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        req = request.args.to_dict()
        print(req)
    data = {}
    print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    build = render_template('component/build.html', data= data)
    content = render_template('layout/2.html', header=header, content=build, footer=footer)
    return render_template('index.html', content=content)

order_bp = Blueprint('order_bp', __name__, template_folder="./views")
leader_bp.register_blueprint(order_bp, url_prefix='/order')
@order_bp.route('/customer', methods=['GET', 'POST'])
def orderCustomer():
    header = render_template('component/header.html')
    content = """<h1>Trang mà leader nhận các đơn đặt ô tô của khách hàng, sau đó khởi động cho manager quản lý</h1>"""
    data = {
        "myorder": dbms.selectBusinessOrders()
    }
    content = render_template('pages/myorder.html',data=data)
    content = render_template('layout/1.html', header=header, content = content)
    return render_template('index.html', content=content)
@order_bp.route('/supplier', methods=['GET', 'POST'])
def orderSupplier():
    header = render_template('component/header.html')
    content = """<h1>Trang mà leader đang đại diện doanh nghiệp đặt hàng nhà cung cấp</h1>"""
    content = render_template('layout/1.html', header=header, content = content)
    return render_template('index.html', content=content)


@leader_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('leader_bp.home'))
