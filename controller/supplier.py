from flask import Blueprint, request, render_template, session, redirect, url_for
from model.dbms import dbms
from controller.main import TOKEN, defineToken

supplier_bp = Blueprint('supplier_bp', __name__, template_folder="./views")

@supplier_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign:
        return redirect(url_for('main_bp.login'))

@supplier_bp.route('/', methods=['GET', 'POST'])
@supplier_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('layout/0.html', header=header)
    return render_template('index.html', content=content)

@supplier_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('supplier_bp.home'))
