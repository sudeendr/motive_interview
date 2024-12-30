import csv

import requests

from .models import City, db


def load_data_into_db(csv_filepath):

    #response=requests.get(csv_filepath)

    with open(csv_filepath, 'r') as f:
        reader= csv.DictReader(f)

        for row in reader:
            id=row.get('ID')
            city_name=row.get('CITY')
            lat=row.get('LATITUDE')
            lon=row.get('LONGITUDE')
            state_name=row.get('STATE_NAME')

            city_obj = City(id=id, city_name=city_name, lat=lat, lon=lon, state_name=state_name)

            db.session.add(city_obj)

        db.session.commit()



def get_city_by_id(id):
    city_obj = City.query.filter(City.id.like(id)).first()

    if city_obj:
        return city_obj

    return None
