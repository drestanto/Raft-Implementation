from bottle import route, run

@route('/api/search_prime/:name')
def index(name):
    return '<b>Hello %s!</b>' % name
    
@route('/api/catch_request/:name')
def index(name):
    return '<b>Hellosss %s!</b>' % name

run(host='localhost', port=5000)


