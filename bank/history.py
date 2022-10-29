from datetime import datetime
from account import Account


class History:
    def __init__(self, account: Account):
        self.account = account
        self.history: list[dict] = []

    def update(self, log: dict) -> None:
        self.history.append(log)

    def last_operation(self) -> dict:
        pass

    def get_history(self) -> list[dict]:
        pass

    def ready_to_clear(self) -> bool:
        now = datetime.now()
        return (self.last_operation - now > datetime(10) and
                self.account.opening_date - now > datetime(50))

    def clear(self):
        if self.ready_to_clear():
            pass
