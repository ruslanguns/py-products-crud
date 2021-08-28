import connexion
from flask_cors import CORS
from os import environ as env
import src.config.config as config
from database.ma import ma
from database.db import db


cx_app = connexion.App(
    "__name__",
    options={'swagger_url': '/'},
    specification_dir='./'
)
cx_app.add_api('swagger.yml', base_path='/api/v1.0')

app = cx_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


CORS(app)
db.init_app(app)


@app.before_first_request
def setup():
    db.create_all()


if __name__ == '__main__':
    ma.init_app(app)
    app.run(port=config.PORT, debug=config.DEBUG, use_reloader=config.RELOAD)
