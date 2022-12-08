from flask import Blueprint, request, render_template, session, redirect, url_for, g
from model.dbms import dbms

main_bp = Blueprint('main_bp', __name__)

sessionCode = [] # {"idlogin": "", "username": "", "role": ""}

@main_bp.before_request
def auth():
    print("before request")
    print(session) # <SecureCookieSession {'idlogin': 'backofficer'}>
    print(request.endpoint) # main_bp.login
    print(request.path) # /login
    if request.endpoint == 'main_bp.login': 
        return 
    if request.endpoint == 'main_bp.signup': 
        return 
    if 'idlogin' not in session:
        return redirect('login')
    exists = False
    for auth in sessionCode:
        if session['idlogin'] == auth["idlogin"]:
            exists = True
            g.user = auth
    if not exists:
        return redirect('/login', code = 302)

@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    header = render_template('component/header.html')
    content = render_template('layout/container.html', header=header)
    return render_template('index.html', content=content)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            if data["username"] == "" or data["password"] == "":
                raise Exception("You need to fulfill all input")
            username, role = dbms.checkSignin(data["username"], data["password"])
            session["idlogin"] = username
            sessionCode.append({"idlogin": username, "username" : username, "role": role})
            return redirect(url_for('customer_bp.home'))
        except Exception as e: 
            loginPage = render_template('pages/login.html', check="fail", msg=str(e))
            return render_template('index.html', content = loginPage)        

    elif request.method == 'GET':
        pass
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
            sessionCode.append({"idlogin": username, "username" : username, "role": role})
            return redirect(url_for('customer_bp.home'))
        except Exception as e: 
            signupPage = render_template('pages/signup.html', check="fail", msg=str(e))
            return render_template('index.html', content = signupPage)

    elif request.method == 'GET':
        pass
    signupPage = render_template('pages/signup.html')
    return render_template('index.html', content=signupPage)


@main_bp.route('/personal-infomation', methods=['GET', 'POST'])
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