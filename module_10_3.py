import random
import threading
from threading import Lock
from threading import Thread
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count = 0
        while count < 100:
            random_number = random.randint(50, 500)
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}\n')
            time.sleep(0.01)
            count += 1
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()

    def take(self):
        count = 0
        while count < 100:
            random_number = random.randint(50, 500)
            print(f'Запрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}.\n')
                count += 1
            else:
                print(f'Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
