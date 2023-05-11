"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Vehicles, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    users = User.query.all()
    allusers = list(map(lambda users: users.serialize(),users))

    return jsonify({"users": allusers}), 200

@app.route('/people', methods=['GET'])
def get_all_people():
    people = Characters.query.all()
    allcharacter = list(map(lambda people: people.serialize(),people))

    return jsonify({"people": allcharacter}), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    people = Characters.query.get(people_id)
    character_serialize = people.serialize()

    return jsonify({"people": character_serialize}), 200


@app.route('/planet', methods=['GET'])
def get_all_planet():
    planet = Planets.query.all()
    allplanets = list(map(lambda planet: planet.serialize(),planet))

    return jsonify({"planet": allplanets}), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = Planets.query.get(planet_id)
    planet_serialize = planet.serialize()

    return jsonify({"planet": planet_serialize}), 200



@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicles.query.all()
    allvehicles = list(map(lambda vehicles: vehicles.serialize(),vehicles))

    return jsonify({"vehicles": allvehicles}), 200

@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def get_one_vehicles(vehicles_id):
    vehicles = Vehicles.query.get(vehicles_id)
    vehicles_serialize = vehicles.serialize()

    return jsonify({"vehicles": vehicles_serialize}), 200

@app.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_favorites(user_id):
    favs = Favorites.query.filter_by(user_id = user_id)
    fav_serialize = list(map(lambda favs: favs.serialize(),favs))

    return jsonify({"fav": fav_serialize}), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
