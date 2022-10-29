class Client:
    def __init__(self, first_name: str, last_name: str, cpf: str) -> None:
        self.name = first_name, last_name
        self.cpf = cpf

        self.id = hash(self)
