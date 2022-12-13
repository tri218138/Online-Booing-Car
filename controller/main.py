from flask import Blueprint, request, render_template, session, redirect, url_for, g
from model.dbms import dbms
import string, random

main_bp = Blueprint('main_bp', __name__)

TOKEN = []

def defineToken(idlogin):
    for auth in TOKEN:
        if idlogin == auth["idlogin"]:
            return True, auth
    return False, None

def supply_session_id():
    session_id = ''.join(random.choices(string.digits+string.ascii_uppercase, k=10)) #USBFDAIB13312
    while session_id in TOKEN:
        session_id = ''.join(random.choices(string.digits+string.ascii_uppercase, k=10))
    return session_id

@main_bp.before_request
def auth():
    if request.endpoint == 'main_bp.login':
        return
    if 'idlogin' not in session:
        return redirect(url_for('main_bp.login'))
    global auth
    sign, auth = defineToken(session["idlogin"])
    if not sign:
        return redirect(url_for('main_bp.login'))

@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('layout/1.html', header=header)
    return render_template('index.html', content=content)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        req = request.form.to_dict()
        response = dbms.checkSignin(req["username"], req["password"])
        if response["status"]:
            session["username"] = req["username"]
            idlogin = supply_session_id()
            session["idlogin"] = idlogin
            TOKEN.append({"idlogin": idlogin, "id": response["id"], "username" : req["username"], "role": response["role"]})
            return redirect(url_for(f'{response["role"]}_bp.home'))
        else:
            data = {
                "status": "fail"
            }
            loginPage = render_template('pages/login.html', data= data)
            return render_template('index.html', content = loginPage)        

    loginPage = render_template('pages/login.html')
    return render_template('index.html', content=loginPage)

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            if data["username"] == "" or data["password"] == "" or data["name"] == "" or data["address"] == "" or data["phonenumber"] == "":
                raise Exception("You need to fulfil all input")
            username = data["username"]
            password = data["password"]
            name = data["name"]
            address = data["address"]
            phonenumber = data["phonenumber"]
            if (len(username) < 6 or len(password)<6):
                raise Exception("Length of password and username must be at least 6")
            username, role = dbms.signUpCustomer(username,password,address,phonenumber,name,1)
            session["idlogin"] = username
            TOKEN.append({"idlogin": username, "username" : username, "role": role})
            return redirect(url_for('customer_bp.home'))
        except Exception as e: 
            signupPage = render_template('pages/signup.html', check="fail", msg=str(e))
            return render_template('index.html', content = signupPage)

    elif request.method == 'GET':
        pass
    signupPage = render_template('pages/signup.html')
    return render_template('index.html', content=signupPage)


@main_bp.route('/profile', methods=['GET', 'POST'])
def personalInfomation():
    pass

@main_bp.route('/setting', methods=['GET', 'POST'])
def setting():
    pass

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main_bp.home'))

@main_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404