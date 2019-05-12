class Produto:
    _id = None
    _product = None
    _price = None

    def __init__(self, id, product, price):
        self._id = id
        self._product = product
        self._price = price

    def getId(self):
        return self._id

    def getProduct(self):
        return self._product

    def getPrice(self):
        return self._price
