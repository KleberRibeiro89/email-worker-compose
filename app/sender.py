from bottle import route, run, request


# @route('/', method='POST')
# def send():
#     assunto = request.forms.get('assunto')
#     mensagem = request.forms.get('mensagem')
#     return 'mensagem enfileirada ! Assunto: {} | Mensagem: {}'.format(assunto, mensagem)

@route('/', method='get')
def send():
    return 'teste ok'


if __name__ == '__main__':
    run(host='0.0.0.0', port=8082, debug=True)
