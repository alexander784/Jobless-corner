from flask import   Flask
from flask_restx import Api,Resource
from config import app
from controllers.auth_controller import auth_ns




api = Api(app)
api.add_namespace(auth_ns, path="/auth")


class Index(Resource):
    def get(self):
        return "Welcome to Ralphy!"
    
api.add_resource(Index, "/")

if __name__== "__main__":
    app.run(port=5000, debug=True)