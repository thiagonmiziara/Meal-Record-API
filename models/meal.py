import datetime
from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    dieting = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime.isoformat(),  # Converte para string em formato ISO 8601
            "dieting": self.dieting,
        }
