'''Configuración de la aplicación'''

class Config:
    '''Configuración base'''
    SECRET_KEY = 'CLAVE_SECRETA'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    '''Configuración de desarrollo'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/idgs_802'