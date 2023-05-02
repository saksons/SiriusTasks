"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import sys
from threading import Thread
import time

block = False
def timer(to_time, notification):
    global block

    time.sleep(to_time)
    print(notification)
    block = True
    # print("программа завершается")

def blocker():
    while not block:
        print("а")
        time.sleep(10)


th1 = Thread(target=timer, args=(5, "hello", )).start()
blocker()

