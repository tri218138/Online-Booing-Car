from flask import Flask, render_template
from controller.main import main_bp
from controller.customer import customer_bp
from controller.manager import manager_bp
from controller.supplier import supplier_bp
from controller.designer import designer_bp
from controller.leader import leader_bp


app = Flask(
    __name__,
    template_folder='./views/',
    static_folder="./views/static"
)
app.secret_key = ".."

app.register_blueprint(main_bp)
app.register_blueprint(customer_bp, url_prefix='/customer')
app.register_blueprint(manager_bp, url_prefix='/manager')
app.register_blueprint(supplier_bp, url_prefix='/supplier')
app.register_blueprint(designer_bp, url_prefix='/designer')
app.register_blueprint(leader_bp, url_prefix='/leader')

if __name__ == '__main__':
    # $ flask run --host 0.0.0.0 --port 5000
    # $ flask run --host 0.0.0.0 --port 5001
    # $ flask run --host 0.0.0.0 --port 5002
    # $ flask run --with-threads
    app.run('0.0.0.0', port=5000, debug=True, threaded=True)
