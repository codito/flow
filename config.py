# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE = {
        'name': 'flow.db',
        'engine': 'peewee.SqliteDatabase'
    }


class ProductionConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
