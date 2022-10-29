from client import Client


class Service:
    def __init__(self, name: str, cnpj: str, clients: list[Client] = [], balance: float = 0.0) -> None:
        self.name = name
        self.cnpj = cnpj

        self.clients = clients
        self.balance = balance

        self.id = hash(self)
