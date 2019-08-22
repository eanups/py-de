from sqlalchemy.engine.url import URL
import os
import envbash

envbash.load_envbash('../../local.bash')

url_params = {'drivername': 'postgres',
              'username': os.environ.get('DATABASE_USER'),
              'password': os.environ.get('DATABASE_PWD'),
              'host': os.environ.get('DATABASE_HOST', 'localhost'),
              'port': 5439
              }

print(URL(**url_params))


