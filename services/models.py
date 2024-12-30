from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class City(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.String(100), nullable=False)
    lon = db.Column(db.String(100), nullable=False)
    state_name = db.Column(db.String(100), nullable=False)
