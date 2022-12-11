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
    if request.method == 'POST':
        pass
    data = {
        "models": dbms.getModelsDetail() #[]
    }
    # print(data)
    header = render_template('component/header.html')
    footer = render_template('component/footer.html')
    model = render_template('component/model.html', data= data)
    content = render_template('layout/1.html', header=header, content=model, footer=footer)
    return render_template('index.html', content=content)

order_bp = Blueprint('order_bp', __name__, template_folder="./views")
leader_bp.register_blueprint(order_bp, url_prefix='/order')
@order_bp.route('/customer', methods=['GET', 'POST'])
def orderCustomer():
    header = render_template('component/header.html')
    content = """<h1>Trang mà leader nhận các đơn đặt ô tô của khách hàng, sau đó khởi động cho manager quản lý</h1>"""
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
