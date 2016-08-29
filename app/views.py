from app import app

@app.route('/')
@app.route('/index')
def index():
	user={'nickname': 'Vladyslav'}
	return '''
<html>
	<head>
		<title>My Flask microblog</title>
	</head>
	<body>
		<h1>Hello, ''' +user['nickname'] + '''</h1>
	</body>
</html>
'''
