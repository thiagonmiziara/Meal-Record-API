from flask import Flask, request
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)


@app.route("/meals", methods=["GET"])
def meal_list():
    meals_data = Meal.query.all()
    return {"meals": [meal.to_dict() for meal in meals_data]}


if __name__ == "__main__":
    app.run(debug=True)
