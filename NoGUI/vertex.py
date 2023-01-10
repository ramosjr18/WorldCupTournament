class Vertex:
    def __init__(self, name) -> None:
        self.id = name
        self.adjacent = {}

    def __str__(self) -> str:
        return str(self.id) + 'adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, name, weight = 0):
        self.adjacent[name] = weight

    def get_connection(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, name):
        return self.adjacent[name]