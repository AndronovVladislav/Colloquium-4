#!/usr/bin/env python3

from flask import Flask
from hotels_microservice.hotels_microservice import HotelsMicroservice


if __name__ == '__main__':
    flask_app = Flask(__name__)

    app = HotelsMicroservice('mysql', 'root', 'Guilopni123!', '127.0.0.1', '3306', 'COLLOQUIUM', flask_app)
    app.run()
