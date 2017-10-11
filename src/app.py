# Juliano Carboneri Francisco
from flask_script import Manager
from flask import Flask
from flask import request
from flask import app
from flask import current_app
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	stringHTML = '<h1>Ola Flask Application - Juliano - %s</h1>' % user_agent
#	app_ctx = app.app_context()
#	app_ctx.push()
	stringHTML += '<p>' + current_app.name + '<p>'
#	stringHTML += '<p>' + app.url_map() + '<p>'
	response = make_response(stringHTML)
	response.set_cookie('resposta', '39')
	return response

@app.route('/user/<name>')
def user(name):
	if name.lower() == 'juliano':
		abort(404)
	return '<h1>Ola, %s</h1>' % name

@app.route('/redirect')
def redirecionar():
	return redirect('http://www.cnn.com/')

if __name__ == '__main__':
#	app.run(debug=True)
	manager.run()