import os
import logging
from ConfigParser import ConfigParser

logging.basicConfig(level=logging.INFO)
logging.getLogger('requests').setLevel(logging.WARNING)

config = ConfigParser()
config.read('config.example.ini')
if os.path.isfile('config.ini'):
    config.read('config.ini')

HOST = 'https://mobile-api.senscritique.com'
# HOST = 'https://mobile-api.senscritique.com' # Not accessible though :(

LOGIN = config.get('user', 'login')
PASSWORD = config.get('user', 'password')