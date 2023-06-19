from utils.microservice_component_interface import MicroserviceComponentInterface

from flask import request, make_response
from sqlalchemy import select
from accessify import private, implements


@implements(MicroserviceComponentInterface)
class HotelsInformant:
    def __init__(self, db):
        self.__hotels = db.hotels
        self.__engine = db.engine
        # self.__error_message = 'Error code: 404 - Not found<br>'
        # self.__error_code = 404

    def action(self):
        with self.__engine.connect() as connection:
            connection.begin()
            response = list()
            for hotel in connection.execute(select(self.__hotels)).fetchall():
                print(hotel)
                response.append({'name': hotel[1],
                                 'address': hotel[2],
                                 'price': hotel[4],
                                 'rate': hotel[3],
                                 })

            return response

    @private
    def make_error(self, error_description):
        pass

    @private
    def validate_data(self, **kwargs):
        pass