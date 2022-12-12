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

@customer_bp.route('/build', methods=['GET', 'POST'])
def build():
    if request.method == 'POST':
        data = json.loads(request.data)
        # add database bill
        return Response('success', 200)
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

@customer_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('customer_bp.home'))
