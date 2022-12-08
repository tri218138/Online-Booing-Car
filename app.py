from flask import Flask, render_template
from controller.main import main_bp
from controller.customer import customer_bp
from controller.manager import manager_bp
from controller.supplier import supplier_bp
from controller.designer import designer_bp


app = Flask(
    __name__,
    template_folder='./views/',
)
app.secret_key = ".."

app.register_blueprint(main_bp)
app.register_blueprint(customer_bp, url_prefix='/customer')
app.register_blueprint(manager_bp, url_prefix='/manager')
app.register_blueprint(supplier_bp, url_prefix='/supplier')
app.register_blueprint(designer_bp, url_prefix='/designer')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
