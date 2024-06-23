from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Postrole
from marshmallow_schema import PostroleSchema

openrole_ns = Namespace('openrole', description="Namespace for openrole")

openrole_model = openrole_ns.model(

    "Openrole",
    {
        "id": fields.Integer(),
        "role_name": fields.String(required=True),
        "description": fields.String(),
        "job_type": fields.String(),
        "duration": fields.String()
    }
)

@openrole_ns.route("/openrole")
class OpenroleResource(Resource):
    @openrole_ns.expect(openrole_model)
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

            query = Postrole.query

            if role_name:
                query = query.filter_by(role_name=role_name)
            if description:
                query = query.filter_by(description=description)
            if job_type:
                query = query.filter_by(job_type=job_type)
            if duration:
                query = query.filter_by(duration=duration)

            roles = query.all()

            if not roles:
                return jsonify({"message": "No roles found matching the criteria"}), 404

            postrole_schema = PostroleSchema(many=True)
            response = postrole_schema.dump(roles)

            return jsonify({"roles": response}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
