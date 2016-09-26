from bottle import route, run, static_file

@route('/')
def home():
	return static_file('index.html', root='.')

run(host='localhost', port=9999) 