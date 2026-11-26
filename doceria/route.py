import os

from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/', method='GET')
def action_index():
    return ctl.render('index')


@app.route('/pedido', method='POST')
def action_pedido():
    corpo, status = ctl.criar_pedido(request.json)
    response.status = status
    return corpo


@app.route('/healthz', method='GET')
def healthz():
    response.content_type = 'text/plain'
    return 'ok'


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=int(os.getenv('PORT', 8080)), debug=True)
