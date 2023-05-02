"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""


from threading import Thread
import time


stop = False
def check_code():
    global stop
    code = int(input())
    if code == 123:
        print("Бомба разминирована")
    else:
        print("Вы взорвались")
    stop = True

def quikly():
    while not stop:
        print("Вводите быстрее")
        time.sleep(3)


th1 = Thread(target=check_code, args=()).start()
th2 = Thread(target=quikly, args=()).start()