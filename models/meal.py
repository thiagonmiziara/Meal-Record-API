import datetime
from app import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    date_and_time = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.now
    )
    dieting = db.Column(db.Boolean, nullable=False, default=False)
