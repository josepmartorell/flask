from flaskproject import db
from datetime import datetime


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(500), nullable=False)
    detail = db.Column(db.Text())
    created_date = db.Column(db.DateTime())
    last_modified = db.Column(db.DateTime())
    is_deleted = db.Column(db.Boolean())

    def __init__(self, subject, detail):
        self.subject = subject
        self.detail = detail
        self.created_date = datetime.now()
        self.last_modified = datetime.now()
        self.is_deleted = False

    def edit(self, subject, detail):
        self.subject = subject
        self.detail = detail
        self.last_modified = datetime.now()

    def delete(self):
        self.last_modified = datetime.now()
        self.is_deleted = True
