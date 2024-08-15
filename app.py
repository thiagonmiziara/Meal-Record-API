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


@app.route("/meal/<int:meal_id>", methods=["GET"])
def meal_by_id(meal_id):
    meal = Meal.query.get(meal_id)
    if not meal:
        return {"error": "Meal not found"}, 404
    return meal.to_dict()


if __name__ == "__main__":
    app.run(debug=True)
