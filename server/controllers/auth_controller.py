import logging
from flask import jsonify, request, make_response
from flask_restx import Namespace, fields, Resource
from config import db
from models import User
from werkzeug.security import generate_password_hash
from marshmallow_schema import user_schema
from flask_jwt_extended import create_access_token, create_refresh_token

# Configure logging
# logging.basicConfig(level=logging.DEBUG)

auth_ns = Namespace('auth', description="A namespace for auth")

signup_model = auth_ns.model(
    'SignUp',
    {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
        "confirm_password": fields.String(required=True)
    }
)

login_model = auth_ns.model(
    'Login',
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    }
)

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        try:
            data = request.json
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirm_password")

            if not username or not email or not password or not confirm_password:
                return make_response(jsonify({"error": "All fields are required"}), 400)

            if password != confirm_password:
                return make_response(jsonify({"error": "Passwords must match"}), 400)

            if isinstance(password, bytes):
                password = password.decode("utf-8")

            new_user = User(
                username=username,
                email=email,
                _password_hash=generate_password_hash(password)
            )
            db.session.add(new_user)
            db.session.commit()

            return make_response(jsonify(user_schema.dump(new_user)), 201)

        except ValueError as e:
            return make_response(jsonify({"error": str(e)}), 500)
        except Exception as e:
            # logging.error("An error occurred during signup", exc_info=True)
            return make_response(jsonify({"error": "An error occurred"}), 500)

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        try:
            data = request.json
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return make_response(jsonify({"error": "Username and password are required"}), 400)

            # logging.debug(f"Username: {username}, Password: {password}")

            db_user = User.query.filter_by(username=username).first()
            if db_user is None:
                # logging.debug("User not found")
                return make_response(jsonify({"error": "Invalid username or password"}), 401)

            # logging.debug(f"Found user: {db_user}")

            if db_user.verify_password(password):
                access_token = create_access_token(identity=db_user.username)
                refresh_token = create_refresh_token(identity=db_user.username)

                # logging.debug(f"Tokens created: Access - {access_token}, Refresh - {refresh_token}")

                return make_response(jsonify({
                    "message": "Login successful",
                    "tokens": {
                        "access": access_token,
                        "refresh": refresh_token
                    },
                    "user": user_schema.dump(db_user)
                }), 200)

            return make_response(jsonify({"error": "Invalid username or password"}), 401)

        except ValueError as e:
            return make_response(jsonify({"error": str(e)}), 500)
        except Exception as e:
            # logging.error("An error occurred during login", exc_info=True)
            return make_response(jsonify({"error": "An error occurred"}), 500)
