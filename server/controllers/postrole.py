from flask_restx import Namespace, Resource, fields
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Postrole
from config import db
from marshmallow_schema import PostroleSchema

postrole_ns = Namespace('postrole', description="Namespace for postrole")

postrole_model = postrole_ns.model(
    "Postrole",
    {
        "role_name": fields.String(required=True),
        "description": fields.String(),
        "job_type": fields.String(),
        "duration": fields.String()
    }
)

@postrole_ns.route("/postrole")
class PostroleResource(Resource):
    @postrole_ns.expect(postrole_model)
    @jwt_required()
    def post(self):
        try:
            data = request.json
            role_name = data.get("role_name")
            description = data.get("description")
            job_type = data.get("job_type")
            duration = data.get("duration")

            user_identity = get_jwt_identity()
            user = User.query.filter_by(username=user_identity).first()

            if not user:
                return jsonify({"message": "User not found"}), 404

            existing_postrole = Postrole.query.filter_by(role_name=role_name).first()

            if existing_postrole:
                return jsonify({"message": "Role with this name already exists"}), 400

            new_postrole = Postrole(
                role_name=role_name,
                description=description,
                job_type=job_type,
                duration=duration
            )

            db.session.add(new_postrole)
            db.session.commit()

            postrole_schema = PostroleSchema()
            response = postrole_schema.dump(new_postrole)

            return make_response(jsonify({
                "message": "Role posted successfully",
                "postrole": response
            }), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
