from sqlalchemy import Table, Column, VARCHAR, ForeignKey, create_engine, MetaData, DECIMAL, TEXT, INT, TIMESTAMP, \
    BOOLEAN
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database


class DB:
    def __init__(self, dialect, user, password, host, port, db):
        self.__metadata = MetaData()
        self.__engine = create_engine(
            '{0}+pymysql://{1}:{2}@{3}:{4}/{5}'.format(dialect, user, password, host, port, db))

        if not database_exists(self.__engine.url):
            create_database(self.__engine.url)

        self.__hotels = Table('hotels', self.__metadata,
                             Column('id', INT, primary_key=True, autoincrement=True),
                             Column('name', VARCHAR(50), nullable=False, unique=True),
                             Column('address', VARCHAR(100), nullable=False, unique=True),
                             Column('rate', DECIMAL, nullable=False),
                             Column('price', DECIMAL, nullable=False),
                             Column('description', VARCHAR(512), nullable=False),
                             Column('features', VARCHAR(512), nullable=False),
                             )
        self.__reviews = Table('reviews', self.__metadata,
                             Column('id', INT, primary_key=True, autoincrement=True),
                             Column('hotel_id', ForeignKey('hotels.id'), nullable=False),
                             Column('description', VARCHAR(512), nullable=False),
                             Column('rate', DECIMAL, nullable=False),
                             )

        self.__booking = Table('booking', self.__metadata,
                             Column('id', INT, primary_key=True, autoincrement=True),
                             Column('hotel_id', ForeignKey('hotels.id'), nullable=False),
                             Column('in', VARCHAR(512), nullable=False),
                             Column('out', VARCHAR(512), nullable=False),
                             )

        # self.__metadata.drop_all(self.__engine)
        self.__metadata.create_all(self.__engine)

    @property
    def hotels(self):
        return self.__hotels

    @hotels.setter
    def hotels(self, *args, **kwargs):
        raise RuntimeError('Changing the database from the outside is prohibited')

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, *args, **kwargs):
        raise RuntimeError('Changing the database from the outside is prohibited')

    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, *args, **kwargs):
        raise RuntimeError('Changing the database from the outside is prohibited')

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, *args, **kwargs):
        raise RuntimeError('Changing the database from the outside is prohibited')

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, *args, **kwargs):
        raise RuntimeError('Changing the database from the outside is prohibited')