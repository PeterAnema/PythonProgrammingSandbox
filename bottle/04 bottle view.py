from bottle import route, run, view

@route('/hello')
@route('/hello/<name>')
@view('hello_template')
def hello(name='World'):
    return dict(name=name)


run(host='localhost', port=8080, debug=True)