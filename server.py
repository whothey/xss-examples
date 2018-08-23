from os import getenv
from bottle import get, post, request, redirect, view, run

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
@view('static/persistent')
def chat():
    return { 'messages': CHAT, 'last_user': request.query.u };


@post('/xss/persistent')
def send_message():
    user  = request.forms.get('user')
    msg   = request.forms.get('message')
    entry = (user, msg)
    CHAT.append(entry)

    return redirect('/xss/persistent?u='+user)


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
    run(host=getenv('HOST_ADDR', 'localhost'), port=getenv('PORT', 3000))
