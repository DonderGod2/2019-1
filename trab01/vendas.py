class Venda:
    _idClient = None
    _idProduct = None
    _amount = None
    _total = None

    def __init__(self, idClient, idProduct, amount, total):
        self._idClient = idClient
        self._idProduct = idProduct
        self._amount = amount
        self._total = total

    def getIdClient(self):
        return self._idClient

    def getIdProduct(self):
        return self._idProduct

    def getAmount(self):
        return self._amount

    def getTotal(self):
        return self._total
