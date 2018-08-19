from os import getenv
from bottle import route, request, view, run

CHAT = [('Anonymous', 'Hello!')]

@route('/')
@view('static/home')
def index():
    return {
        'examples': {
            '/xss/reflected': 'Reflected',
            '/xss/persistent': 'Persistent',
            '/xss/dom': 'DOM-XSS'
        }
    }


@route('/xss/persistent')
def chat():
    return 'chat';


@route('/xss/reflected')
@view('static/reflected')
def search():
    return {
        'query': request.query.q
    }


@route('/xss/dom')
def dom():
    return 'your query?';


@route('/xss/self')
def selfxss():
    return 'are you really going to do this?';


if __name__ == '__main__':
    run(host='localhost', port=getenv('PORT', 3000))
