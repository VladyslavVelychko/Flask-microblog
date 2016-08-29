from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user={'nickname': 'Vladyslav'}
	posts=[
		{
		    'author': {'nickname': 'Andrey'},
		    'body': 'Beautiful morning in Kyiv'

		},
		{
		    'author': {'nickname': 'Marine'},
		    'body': 'It was a great summer. See you soon, NYC!'

}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
