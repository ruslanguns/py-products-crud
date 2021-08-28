from os import environ as env

if env.get('FLASK_ENV') == 'development':
    env.setdefault('DEBUG', 'True')
    env.setdefault('RELOAD', 'True')

ENV = env.get('FLASK_ENV')
PORT = int(env.get('PORT', '5000'))
DEBUG = env.get('DEBUG', 'False') == 'True'
RELOAD = env.get('RELOAD', 'False') == 'True'
