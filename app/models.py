from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(128), nullable=False)
    lname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128),nullable=False)
    username = db.Column(db.String(128),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)


    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<user {self.id} | {self.username}"

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(128),nullable=False)
    last_name= db.Column(db.String(128),nullable=False)
    phone_number = db.Column(db.String(128),nullable=False)
    address = db.Column(db.String(128),nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)