from flask import Blueprint, request, render_template, session, redirect, url_for
from model.dbms import dbms
from controller.main import TOKEN, defineToken

customer_bp = Blueprint('customer_bp', __name__, template_folder="./views")

@customer_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign:
        return redirect(url_for('main_bp.login'))

@customer_bp.route('/', methods=['GET', 'POST'])
@customer_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('layout/1.html', header=header)
    return render_template('index.html', content=content)

@customer_bp.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        pass
    data = {
        "models": dbms.getModelsDetail() #[]
    }
    print(data)
    header = render_template('component/header.html')
    model = render_template('component/model.html', data= data)
    content = render_template('layout/1.html', header=header, content=model)
    return render_template('index.html', content=content)
@customer_bp.route('/build', methods=['GET','POST'])
def build():
    data = {
        "interior": dbms.selectComponentByType("interior"), #[{"":""}]
        "exterior": dbms.selectComponentByType("exterior")
    }
    demo = ""
    if request.method == "POST":
        req = request.form.to_dict()
        print(req)
        pass
    if request.method == "GET":
        req = request.args.to_dict()
        if "exterior" in req:
            carComponent = dbms.selectComponentById(req["exterior"])
            demo = f"""<img src="{carComponent['url']}" class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />"""
    header = render_template('component/header.html')
    operator = render_template('component/operator.html', data= data)
    content = render_template('layout/0.html', header=header, content=demo, operator=operator)
    return render_template('index.html', content=content)


@customer_bp.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        pass
    data = {}
    print(data)
    header = render_template('component/header.html')
    build = render_template('component/build.html', data= data)
    content = render_template('layout/2.html', header=header, content=build)
    return render_template('index.html', content=content)

@customer_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('customer_bp.home'))
