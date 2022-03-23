import os

import sqlalchemy
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# db = Database(os.environ['DATABASE_URL'])
# db = Database('postgresql://postgres:postgres@0.0.0.0:5432/test_db')

metadata = sqlalchemy.MetaData()
