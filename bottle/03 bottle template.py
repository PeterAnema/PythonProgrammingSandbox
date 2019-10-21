from bottle import route, run, template


@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)


run(host='localhost', port=8080, debug=True)