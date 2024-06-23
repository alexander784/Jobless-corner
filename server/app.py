from flask import   Flask
from flask_restx import Api,Resource
from config import app
from controllers.auth_controller import auth_ns
from controllers.postrole import postrole_ns
from controllers.openrole import openrole_ns




api = Api(app)
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(postrole_ns, path="/postrole")
api.add_namespace(openrole_ns, path="/openrole")


class Index(Resource):
    def get(self):
        return "Welcome to Ralphy!"
    
api.add_resource(Index, "/")

if __name__== "__main__":
    app.run(port=5000, debug=True)