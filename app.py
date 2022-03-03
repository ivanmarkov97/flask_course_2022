from flask import Flask
from infrastructure.web.requests.routes import requests_app


def create_app() -> Flask:
	app = Flask(__name__)
	app.config['DB_CONFIG'] = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'root'}
	app.register_blueprint(requests_app, url_prefix='/requests')
	return app


if __name__ == '__main__':
	application = create_app()
	application.run(host='127.0.0.1', port=5001)
