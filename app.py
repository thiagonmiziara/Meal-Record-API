import datetime
from flask import Flask, request
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://admin:admin123@127.0.0.1:3306/meal-record"
)
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


@app.route("/meal", methods=["POST"])
def create_meal():
    data = request.get_json()

    if len(data["description"]) > 120:
        return {"error": "Description must be less than 120 characters"}, 400

    new_meal = Meal(
        name=data["name"],
        description=data["description"],
        datetime=datetime.datetime.now(),
        dieting=data.get("dieting", False),
    )
    db.session.add(new_meal)
    db.session.commit()
    return {"message": "Meal created successfully"}


@app.route("/meal/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return {"error": "Meal not found"}, 404

    data = request.get_json()

    if not data:
        return {"error": "No data provided"}, 400

    if "description" in data and len(data["description"]) > 120:
        return {"error": "Description must be less than 120 characters"}, 400

    meal.name = data.get("name", meal.name)
    meal.description = data.get("description", meal.description)
    meal.datetime = data.get("datetime", meal.datetime)
    meal.dieting = data.get("dieting", meal.dieting)
    db.session.commit()
    return {"message": "Meal updated successfully"}


@app.route("/meal/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)
    if not meal:
        return {"error": "Meal not found"}, 404
    db.session.delete(meal)
    db.session.commit()
    return {"message": "Meal deleted successfully"}


if __name__ == "__main__":
    app.run(debug=True)
