from models import User,Postrole,Openrole
from marshmallow import fields
from config import ma


class UserSchema(ma.Schema):
    class Meta:
        model = User

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, unique=True)
    email = fields.Email(required=True, unique=True)
    _password_hash = fields.Str(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class PostroleSchema(ma.Schema):
    class Meta:
        model = Postrole
    id = fields.Int(dump_only=True)
    role_name = fields.Str(required=True)
    description = fields.Str(required=True)
    job_type = fields.Str(required=True)
    duration=fields.Str(required=True)


Postrole_schema = PostroleSchema()
Postroles_schema = PostroleSchema(many=True)


class OpenroleSchema(ma.Schema):
    class Meta:
        model = Openrole

    id = fields.Int(dump_only=True)
    role_name = fields.Str(required=True)
    description = fields.Str(required=True)
    job_type = fields.Str(required=True)
    duration=fields.Str(required=True)



