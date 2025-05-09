from typing import List
from enum import Enum

# -----------------------
# User Class
# -----------------------
class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.bank_accounts: List[BankAccount] = []

    def link_bank_account(self, account: 'BankAccount'):
        self.bank_accounts.append(account)

# -----------------------
# BankAccount Class
# -----------------------
class BankAccount:
    def __init__(self, account_number: str, bank_name: str, balance: float):
        self.account_number = account_number
        self.bank_name = bank_name
        self.balance = balance

# -----------------------
# Transaction Class
# -----------------------
class TransactionStatus(Enum):
    INITIATED = 'INITIATED'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'

class Transaction:
    def __init__(self, txn_id: str, sender: User, receiver: User, amount: float):
        self.txn_id = txn_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = TransactionStatus.INITIATED

# -----------------------
# UPI Gateway
# -----------------------
class UPIGateway:
    def process_payment(self, sender_account: BankAccount, receiver_account: BankAccount, amount: float) -> bool:
        if sender_account.balance >= amount:
            sender_account.balance -= amount
            receiver_account.balance += amount
            return True
        return False

# -----------------------
# Ledger
# -----------------------
class Ledger:
    def __init__(self):
        self.entries: List[Transaction] = []

    def record_transaction(self, transaction: Transaction):
        self.entries.append(transaction)

# -----------------------
# Notification Service
# -----------------------
class NotificationService:
    def send(self, user: User, message: str):
        print(f"Notify {user.name}: {message}")

# -----------------------
# GooglePayApp (Main Service)
# -----------------------
class GooglePayApp:
    def __init__(self):
        self.ledger = Ledger()
        self.upi_gateway = UPIGateway()
        self.notification_service = NotificationService()

    def transfer_money(self, sender: User, sender_account: BankAccount,
                       receiver: User, receiver_account: BankAccount, amount: float) -> Transaction:
        txn = Transaction("TXN123", sender, receiver, amount)

        if self.upi_gateway.process_payment(sender_account, receiver_account, amount):
            txn.status = TransactionStatus.SUCCESS
            self.ledger.record_transaction(txn)
            self.notification_service.send(sender, f"₹{amount} sent to {receiver.name}")
            self.notification_service.send(receiver, f"₹{amount} received from {sender.name}")
        else:
            txn.status = TransactionStatus.FAILED
            self.notification
