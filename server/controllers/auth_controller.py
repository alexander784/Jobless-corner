from flask import jsonify,request,make_response
from flask_restx import Namespace,fields,Resource
from config import db
from models import User
from werkzeug.security import generate_password_hash
from marshmallow_schema import user_schema



auth_ns = Namespace('auth', description="A namespace for auth")


signup_model = auth_ns.model(
    'SignUp',
    {
        "username":fields.String(),
        "email":fields.String(),
        "password:":fields.String()
    }
)
login_model = auth_ns.model(
    'Login',
    {
        "username":fields.String(),
        "password":fields.String()
    }
)

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        try:
            data = request.json
            password = data.get("password")
            confirm_password = data.get("confirm_password")

            if password == confirm_password:
                if isinstance(password, bytes):
                    password = password.decode("utf-8")
                    
                new_user = User(
                    username=data.get("username"),
                    email=data.get("email"),
                    _password_hash=generate_password_hash(password)


                )
                db.session.add(new_user)
                db.session.commit()

                return make_response(jsonify(user_schema.dump(new_user)), 201)
            return make_response(jsonify({"error":"Password must match"}))
        
        except ValueError as e:
            return make_response(jsonify({"error": str(e)}))
        
