class Config(object):
    DEBUG = False
    TESTING = False
    URL_DATA_SOURCE = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees"


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'


class ProductionConfig(Config):
    pass
