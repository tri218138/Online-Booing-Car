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
        "models": dbms.getModelsDetail()
    }
    print(data)
    header = render_template('component/header.html')
    model = render_template('component/model.html', data= data)
    content = render_template('layout/1.html', header=header, content=model)
    return render_template('index.html', content=content)

@customer_bp.route('/detail', methods=['GET', 'POST'])
def detail():
    if request.method == 'POST':
        pass
    carID = request.args['id']
    data = {
        "car": dbms.getModelByID(carID)
    }
    header = render_template('component/header.html')
    model = render_template('component/detail.html', data= data)
    content = render_template('layout/1.html', header=header, content=model)
    return render_template('index.html', content=content)


@customer_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('customer_bp.home'))
