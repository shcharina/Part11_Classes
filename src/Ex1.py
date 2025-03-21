class Friends:
    def __init__(self, *connections):
        self.connections = set(map(frozenset, connections))

    def add(self, connection: set[str]) -> bool:
        connection = frozenset(connection)
        if connection in self.connections:
            return False
        self.connections.add(connection)
        return True

    def remove(self, connection: set[str]) -> bool:
        connection = frozenset(connection)
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self) -> set[str]:
        return {name for connection in self.connections for name in connection}

    def connected(self, name: str) -> set[str]:
        return {person for connection in self.connections if name in connection for person in connection if person != name}