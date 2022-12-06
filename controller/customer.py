from flask import Blueprint, request, render_template, session, redirect, url_for, g

customer_bp = Blueprint('customer_bp', __name__, template_folder="./views")

@customer_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))

@customer_bp.route('/', methods=['GET', 'POST'])
@customer_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('layout/container.html', header=header)
    return render_template('index.html', content=content)

@customer_bp.route('/model', methods=['GET','POST'])
def model():
    if request.method == 'POST':
        req = request.form.to_dict()
        if req["request"] == "update":
            # dbms.updateModelDetail(req["id"], req)
            pass
    data = None #query data
    header = render_template('component/header.html')
    gallery = render_template('component/model.html', data = data)
    content = render_template('layout/container.html', header=header, content=gallery)
    return render_template('model', content=content)

@customer_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('customer_bp.home'))
