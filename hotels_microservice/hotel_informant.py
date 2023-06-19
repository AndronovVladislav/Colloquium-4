from utils.microservice_component_interface import MicroserviceComponentInterface
from flask import request, make_response
from sqlalchemy import select
from accessify import private, implements


# @implements(MicroserviceComponentInterface)
class HotelInformant:
    def __init__(self, db):
        self.__hotels = db.hotels
        self.__engine = db.engine
        # self.__error_message = 'Error code: 404 - Not found<br>'
        # self.__error_code = 404

    def action(self, id):
        with self.__engine.connect() as connection:
            connection.begin()
            hotel_info = connection.execute(select(self.__hotels)
                                            .where(self.__hotels.c.id == id))\
                                            .fetchone()
            response = {'name': hotel_info[1],
                        'address': hotel_info[2],
                        'price': hotel_info[4],
                        'rate': hotel_info[3],
                        'description': hotel_info[5],
                        'features': hotel_info[6]}

            return response

    @private
    def make_error(self, error_description):
        pass

    @private
    def validate_data(self, **kwargs):
        pass
