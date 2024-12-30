from flask import Flask, jsonify, request
from services.geocoding_service import get_address_from_coordinates
from services.models import db

app = Flask(__name__)

from services.db_service import load_data_into_db  , get_city_by_id


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#CSV_FILEPATH='https://raw.githubusercontent.com/kelvins/US-Cities-Database/main/csv/us_cities.csv'
db.init_app(app)
app.app_context().push()
db.create_all()


CSV_FILEPATH='us_cities.csv'


@app.route('/api/address', methods=['GET'])
def api_address():

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if lat is None or lon is None:
        return jsonify({"error": "Missing lat or lon"}), 400


    address = get_address_from_coordinates(lat, lon)

    return jsonify(address)


load_data_into_db(CSV_FILEPATH)

@app.route('/api/address_db', methods=['GET'])
def api_address_db():


    id = request.args.get('id')

    data=get_city_by_id(id)

    return jsonify(data)






if __name__ == '__main__':
    app.run(debug=True)