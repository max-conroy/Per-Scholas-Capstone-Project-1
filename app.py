from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return  'You are at the home page'

@app.route('/about')
def about():
	return 'You are at the about page'

@app.route('/dostuff')
def dostuff():
	return 'App does stuff here'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
