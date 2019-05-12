class Cliente:
    _id = None
    _name = None

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def getId(self):
        return self._id

    def getName(self):
        return self._name
