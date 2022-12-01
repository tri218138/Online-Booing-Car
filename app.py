from flask import Flask

app = Flask(__name__, template_folder='view/templates')

# from controller.person import person
from controller.controller import *

if __name__ == "__main__":
    app.run(debug=True)

# ref: https://ourtechroom.com/tech/use-google-drive-image-in-html-and-website/
# custom marker https://docs.mapbox.com/mapbox-gl-js/api/markers/