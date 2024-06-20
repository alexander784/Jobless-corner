from config import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    postrole_id = db.Column(db.Integer, db.ForeignKey('postroles.id'), nullable=True)
    postrole = db.relationship("Postrole", backref="users", lazy=True)

    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


class Postrole(db.Model):
    __tablename__ = "postroles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    job_type = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)


class Openrole(db.Model):
    __tablename__ = "openroles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    job_type = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
