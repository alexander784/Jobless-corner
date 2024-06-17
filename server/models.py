
from config import db


class User():
    
 __table_name__ = "users"

 username = db.Column(db.String)
 email = db.Column(db.String, nullable=False,unique=True)
 password = db.Column(db.String, nullable=False, unique=True)


class Postrole():
 
 __table_name__ = "postroles"

 role_name = db.Column(db.String, nullable=False, unique=True)
 description = db.Column(db.String, nullable=False)
 job_type = db.Column(db.String, nullable=False)
 duration = db.Column(db.String, nullable=False,)

class Openrole():
  
  __table_name__ = "openroles"

  role_name = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  job_type = db.Column(db.String, nullable=False)
  duration = db.Column(db.String, nullable=False,)
  





