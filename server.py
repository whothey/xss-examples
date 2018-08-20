from os import getenv
from bottle import get, request, view, run

CHAT = [('Anonymous', 'Hello!')]

@get('/')
@view('static/home')
def index():
    return {
        'examples': {
            '/xss/reflected': 'Reflected',
            '/xss/persistent': 'Persistent',
            '/xss/dom': 'DOM-XSS'
        }
    }


@get('/xss/persistent')
def chat():
    return 'chat';


@get('/xss/reflected')
@view('static/reflected')
def search():
    return {
        'query': request.query.q
    }


@get('/xss/dom')
def dom():
    return 'your query?';


@get('/xss/self')
def selfxss():
    return 'are you really going to do this?';


if __name__ == '__main__':
    run(host='localhost', port=getenv('PORT', 3000))
