#!/usr/bin/env python3
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route("/")
def index():
    return "<h1>Code challenge</h1>"

class Restaurants(Resource):
    def get(self):
        restaurants = [
            restaurant.to_dict(only=("id", "name", "address"))
            for restaurant in Restaurant.query.all()
        ]
        return make_response(restaurants, 200)

class RestaurantById(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response({"error": "Restaurant not found"}, 404)
        return make_response(
            restaurant.to_dict(
                only=(
                    "id",
                    "name",
                    "address",
                    "restaurant_pizzas.id",
                    "restaurant_pizzas.pizza_id",
                    "restaurant_pizzas.price",
                    "restaurant_pizzas.restaurant_id",
                    "restaurant_pizzas.pizza",
                )
            ),
            200,
        )

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response({"error": "Restaurant not found"}, 404)
        db.session.delete(restaurant)
        db.session.commit()
        return make_response({}, 204)

class Pizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict(only=("id", "name", "ingredients")) for pizza in Pizza.query.all()]
        return make_response(pizas, 200)

class RestaurantPizzas(Resource):
    def post(self):
        data = request.get_json()
        try:
            # Validate that Pizza and Restaurant exist
            if not Pizza.query.get(data["pizza_id"]):
                return make_response({"errors": ["Pizza not found"]}, 404)
            if not Restaurant.query.get(data["restaurant_id"]):
                return make_response({"errors": ["Restaurant not found"]}, 404)

            restaurant_pizza = RestaurantPizza(
                price=data["price"],
                pizza_id=data["pizza_id"],
                restaurant_id=data["restaurant_id"],
            )
            db.session.add(restaurant_pizza)
            db.session.commit()
            return make_response(
                restaurant_pizza.to_dict(
                    only=(
                        "id",
                        "price",
                        "pizza_id",
                        "restaurant_id",
                        "pizza",
                        "restaurant",
                    )
                ),
                201,
            )
        except ValueError as e:
            return make_response({"errors": [str(e)]}, 400)
        except Exception as e:
            return make_response({"errors": ["Failed to create RestaurantPizza"]}, 400)

api.add_resource(Restaurants, "/restaurants")
api.add_resource(RestaurantById, "/restaurants/<int:id>")
api.add_resource(Pizzas, "/pizzas")
api.add_resource(RestaurantPizzas, "/restaurant_pizzas")

if __name__ == "__main__":
    app.run(port=5555, debug=True)