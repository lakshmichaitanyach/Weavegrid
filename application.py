from flask import Flask
from flask_restful import Api
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from resources.routes import initialize_routes
from resources.errors import custom_errors

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app, errors= custom_errors)
initialize_routes(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug = True)
            










