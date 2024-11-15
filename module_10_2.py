import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.count = 100
        self.days_fighting = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.count > 0:
            self.days_fighting += 1
            self.count -= self.power
            sleep(1)
            print(f'{self.name} сражается {self.days_fighting} день(дня)..., осталось {self.count} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {self.days_fighting} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
sleep(1)
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы завершены!")
