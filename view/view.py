from flask import render_template, jsonify, get_template_attribute, url_for

class View():
    def __init__(self):
        self.role = ''
    def setRole(self, role_):
        self.role = role_
        self.setHeader()
        # self.setSideBar()
    def setHeader(self):
        self.headerHTML = render_template('header.html', role=self.role)
    def setModelGallery(self, data_):
        self.modelGallery = render_template('model.html', role=self.role, data=data_)
    def setNavBarBuild(self):
        self.navBarBuild = render_template('build/navbar.html')
    def setSideBarBuild(self, data_):
        self.sideBarBuild = render_template('/build/sidebar.html', data=data_)
    def setOrderHTML(self, data_):
        self.orderHTML = render_template('order.html', role=self.role, data=data_)

    def render_template_home(self, data_):
        return render_template('index.html', header=self.headerHTML, gallery = data_)
    def render_template_signin(self, data_):
        signin = render_template('signin.html', check=data_)
        return render_template('index.html', signin = signin)
    def render_template_model(self, data_):
        return render_template('index.html', header=self.headerHTML, gallery = self.modelGallery)
    def render_template_build(self, data_):
        demo = '''
            <img id="demo-img-car" src="http://drive.google.com/uc?export=view&id=1Z2gn9zjGLk599lp8QKKiP4gO1Q724uI8"
                class="w-100 shadow-1-strong rounded mb-4" alt="Boat on Calm Water" />
        '''
        return render_template('index.html', header=self.headerHTML, content=demo, navBarBuild = self.navBarBuild, sidebar=self.sideBarBuild)
    def render_template_order(self, data_):
        return render_template('index.html', header=self.headerHTML, order = self.orderHTML)
    def render_template(self, template, data=None):
        if template == '/':
            return self.render_template_home(data)
        elif template == 'signin':
            return self.render_template_signin(data)
        elif template == 'model':
            return self.render_template_model(data)
        elif template == 'build':
            return self.render_template_build(data)
        elif template == 'order':
            return self.render_template_order(data)

view = View()