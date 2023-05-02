"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""

def get_text_from_file(file):
    full_text = []
    with open(file, 'r', encoding="utf-8") as file:
        text = file.read()
        text = text.replace(',','')
        text = text.replace('.', '')
    for i in text.split('\n'):
        full_text.append(i.split(' '))
    return full_text


def count_words_from_file(file):
    full_text = get_text_from_file(file=file)
    max_words = 0
    max_minus_words = 0

    for a in full_text:
        for b in len(a):
            ...

count_words_from_file("test.txt")