"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""

from threading import Thread
import time
start = time.time()

def first_file():
    with open("Files/file0.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def second_file():
    with open("Files/file1.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def thried_file():
    with open("Files/file2.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def fourth_file():
    with open("Files/file3.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def fifth_file():
    with open("Files/file4.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def sixth_file():
    with open("Files/file5.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def seventh_file():
    with open("Files/file6.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def eighth_file():
    with open("Files/file7.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def nineth_file():
    with open("Files/file8.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

def tenth_file():
    with open("Files/file9.txt", "w", encoding="UTF-8") as file:
        file.write("id:12345")

th1 = Thread(target=first_file, args=()).start()
th1 = Thread(target=second_file, args=()).start()
th1 = Thread(target=thried_file, args=()).start()
th1 = Thread(target=fifth_file, args=()).start()
th1 = Thread(target=sixth_file, args=()).start()
th1 = Thread(target=seventh_file, args=()).start()
th1 = Thread(target=eighth_file, args=()).start()
th1 = Thread(target=nineth_file, args=()).start()
th1 = Thread(target=tenth_file, args=()).start()

print(time.time() - start)