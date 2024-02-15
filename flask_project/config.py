import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
debug = True

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False