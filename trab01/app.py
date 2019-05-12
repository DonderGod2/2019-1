from flask import Flask, url_for, request, json, jsonify
from json import dumps

from cliente import Cliente
from produto import Produto
from vendas import Venda


app = Flask(__name__)

clientes = []
produtos = []
vendas = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/cliente', methods = ['POST', 'GET'])
def api_cliente():
    if(request.method == 'POST'):
        request_data = request.get_json()

        for data in request_data:
            novo_cliente = Cliente(data['id'], data['name'])
            clientes.append(novo_cliente)

        mensagem = { 'err': 'Error creating client'}
        if(novo_cliente != None):
            mensagem = { 'status': 'ok' }

        return jsonify(mensagem)
    elif(request.method == 'GET'):
        mensagem = []
        for cliente in clientes:
            element = { 'id': cliente.getId(), 'name': str(cliente.getName()) }
            mensagem.append(element)
        return jsonify(mensagem)


@app.route('/produto', methods = ['POST', 'GET'])
def api_produto():
    if(request.method == 'POST'):
        request_data = request.get_json()

        for data in request_data:
            novo_produto = Produto(data['id'], data['product'], data['price'])
            produtos.append(novo_produto)

        mensagem = { 'err': 'Error creating client'}
        if(novo_produto != None):
            mensagem = { 'status': 'ok' }

        return jsonify(mensagem)
    elif(request.method == 'GET'):
        mensagem = []
        for produto in produtos:
            element = { 'id': produto.getId(), 'name': str(produto.getProduct()), 'price': produto.getPrice() }
            mensagem.append(element)
        return jsonify(mensagem)


@app.route('/newsale', methods = ['POST'])
def api_sale():
    request_data = request.get_json()

    for produto in produtos:
        if(produto.getId() == request_data['idProduct']):
            amount = request_data['amount']
            total = int(amount) * produto.getPrice()
            nova_venda = Venda(request_data['idClient'], request_data['idProduct'], amount, total)
            vendas.append(nova_venda)

            print(vendas)
    return jsonify({ 'status': 'ok' })


@app.route('/sales/<idClient>', methods = ['GET'])
def api_sales(idClient):
    mensagem = []
    contador = 0
    for venda in vendas:
        if(venda.getIdClient() == int(idClient)):
            element = { 'product': venda.getIdProduct(), 'amount': venda.getAmount(), 'total': venda.getTotal() }
            mensagem.append(element)
            contador = contador + 1

    totalVendas = { 'Total de vendas': contador }
    mensagem.append(totalVendas)
    return jsonify(mensagem)

if __name__ == '__main__':
    app.run()
