from flask import Flask
from flask_restful import Api

import backend.routes


app = Flask(__name__, static_url_path='', static_folder="public")
api = Api(app)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
