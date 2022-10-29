from datetime import datetime
from history import History
from client import Client
from service import Service


class Account:
    def __init__(self, owner: Client, services: list[Service] = [], balance: float = 0.0) -> None:
        self.owner = owner
        self.services = services
        self.balance = balance

        self.opening_date = datetime.now()

        self.history = History(self)
        self.id = hash(self)

    def deposit(self, value: float, is_transfer: bool = False) -> None:
        """Increase an amount of cash on account.

        Args:
            value (float): Amount to be entered into the account.
            inst_transfer (bool, optional): If this operation is a transfer step. Defaults to False.
        """

        # Update the account history
        if not is_transfer:
            self.history.update({
                'type': 'deposit',
                'value': value,
                'date': datetime.now()
            })

        # Update cash
        self.balance += value

    def withdraw(self, value: float, is_transfer: bool = False) -> bool:
        """Withdraw an amount of cash from the account.

        Args:
            value (float): _description_
            is_transfer (bool, optional): If this operation is a transfer step. Defaults to False.

        Returns:
            bool: If the operation was done with success.
        """

        # Validates if the account has sufficient balance
        if self.balance < value:
            return False

        # Update the account history
        if not is_transfer:
            self.history.update({
                'type': 'withdraw',
                'value': value,
                'date': datetime.now()
            })

        # Update cash
        self.balance -= value
        return True

    def transfer_to(self, receiver: 'Account', value: float) -> bool:
        """_summary_

        Args:
            receiver (Account): _description_
            value (float): _description_

        Returns:
            bool: _description_
        """

        if self.withdraw(value, True):
            receiver.deposit(value, True)

            log = {
                'type': 'transfer',
                'sender': self.id,
                'receiver': receiver.id,
                'value': value,
                'date': datetime.now()
            }

            self.history.update(log)
            receiver.history.update(log)

            return True
        return False

    # def payment(self, service: Service, plan_id: int):
    # def pix(self, key_type: str, key: str):

    def extract(self):
        return {
            'id': self.id,
            'date': datetime.now(),
            'balance': self.balance
        }

    def show_extract(self):
        print(
            f"ID: {self.id}",
            f"Name: {' '.join(self.owner.name)}",
            f"CPF: {self.owner.cpf}",
            f"Balance: {self.balance}",
            sep='\t'
        )


if __name__ == '__main__':
    pedo = Client('Pedro', 'Galvão', '622.209.173-39')
    contaDoPedro = Account(pedo)
    ana = Client('Ana Luíza', 'Torres', '123.321.222-11')
    contaDaAna = Account(ana, 9999999999999.99)

    if contaDaAna.transfer_to(contaDoPedro, 10):
        contaDaAna.show_extract()
        contaDoPedro.show_extract()

    if not contaDoPedro.transfer_to(contaDaAna, 100):
        print('Pobre!')
