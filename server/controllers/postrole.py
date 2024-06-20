from flask_restx import Namespace,Resource,fields
from flask import request,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from models import User,Postrole
from config import db
from marshmallow_schema import PostroleSchema




postrole_ns = Namespace('postrole', description="Namespace for postrole")

postrole_model = postrole_ns.model(
    "Postrole",
    {
        "id":fields.Integer(),
        "role_name":fields.String(required=True),
        "description":fields.String(),
        "job_type":fields.String(),
        "duration":fields.String()

    },
)

@postrole_ns.route("/postrole")
class PostroleResource(Resource):
    @postrole_ns.expect(postrole_model)
    @jwt_required()
    def post(self):
        data = request.json
        role_name = data.get("role_name")
        description = data.get("description")
        job_type = data.get("job_type")
        duration = data.get("duration")
        
        user_identity = get_jwt_identity()
        user = User.query.filter_by(username=user_identity).first()


        if not user:
            return jsonify({"message":"User Not found"})
        
        role_name = role_name.query.get(role_name)
        if not role_name:
            return jsonify({"message": "Role_name Not found"})
        
        if not description:
            return jsonify  ({"message":"Description Not found"})
        
        if not job_type:
            return jsonify({"message":"Job Type not found"})
        
        if not duration:
            return jsonify({"message":"duration not found"}), 400
        
        new_postrole = Postrole(role_name=role_name,
                                description = description,
                                job_type = job_type,
                                duration = duration
                                )
        db.session.add(new_postrole)
        db.session.commit()

        result = PostroleSchema.dump(new_postrole)

        return jsonify({"message":"Role Posted Successfully"})




