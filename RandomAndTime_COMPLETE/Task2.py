"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""

import random


peoples = int(input("Число участников сборной _: "))

print(f"Пловец {random.randint(1,peoples)} - пловец {random.randint(1,peoples)}")