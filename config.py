import os


class Config(object):
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'
    DEBUG = False
    TESTING = False
    CWD = os.getcwd()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(CWD, 'profiles.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS_DEFAULT_DEST = os.path.join(CWD, 'uploads')


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevConfig(Config):
    DEBUG = True
