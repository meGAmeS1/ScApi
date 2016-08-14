import os
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.default.ini')
if os.path.isfile('config.ini'):
    config.read('config.ini')

HOST = 'https://mobile-api.senscritique.com'
# HOST = 'https://mobile-api.senscritique.com' # Not accessible though :(

LOGIN = config.get('user', 'login')
PASSWORD = config.get('user', 'password')