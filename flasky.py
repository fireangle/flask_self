from flask_script import Manager
from app import create_app
import os



app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manage=Manager(app)

if __name__=='__main__':
    manage.run()