"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

a = {
    1:1,
    2:3,
    3:3,
    4:4,
    5:5
}
print(id(a), a)
a[1], a[5] = a[5], a[1]
# del a[list(a.items())[1][0]]
print(a.keys()[1])
a["new_key"] = "new_value"
print(id(a), a)