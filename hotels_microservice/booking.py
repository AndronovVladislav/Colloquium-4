from utils.microservice_component_interface import MicroserviceComponentInterface
from flask import request, make_response
from sqlalchemy import insert
from accessify import private, implements


@implements(MicroserviceComponentInterface)
class BookingPoster:
    def __init__(self, db):
        self.__booking = db.booking
        self.__engine = db.engine
        # self.__error_message = 'Error code: 404 - Not found<br>'
        # self.__error_code = 404

    def action(self):
        params = request.get_json()

        with self.__engine.connect() as connection:
            connection.begin()

            connection.execute(insert(self.__booking).values(params))
            connection.commit()

        return 'Success'

    @private
    def make_error(self, error_description):
        pass

    @private
    def validate_data(self, **kwargs):
        pass
