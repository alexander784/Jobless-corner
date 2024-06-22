
from flask_restx import Namespace,fields
from flask import request




openrole_ns = Namespace('openrole', description="A Namespace for openrole")

openrole_model = openrole_ns.model(
    "Postrole",
    {
        "id":fields.Integer(),
        "role_name":fields.String(required=True),
        "description":fields.String(),
        "job_type":fields.String(),
        "duration":fields.String()

    },
)



class OpenroleResource():
    def post():
        data = request.json()

