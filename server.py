from os import getenv
from bottle import route, request, run

CHAT = [('Anonymous', 'Hello!')]

@route('/')
def index():
    return 'This is just a welcome page, please head to intended example: '


@route('/xss/persistent')
def chat():
    return 'chat';


@route('/xss/reflected')
def search():
    return 'your query: ' + request.query.q;


@route('/xss/dom')
def dom():
    return 'your query?';


@route('/xss/self')
def selfxss():
    return 'are you really going to do this?';


if __name__ == '__main__':
    run(host='localhost', port=getenv('PORT', 3000))
