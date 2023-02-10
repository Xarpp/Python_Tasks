import datetime
import random
import string
import os
import csv
import time


# information output

# 1. Вывести на экран текущее название дня недели, название
# месяца и свое имя. Каждое слово должно быть в отдельной

def task_one():
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август",
                   "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

    eng_date = datetime.datetime.now().strftime('%A\n%B')

    ru_weekday = weekdays[int(datetime.datetime.today().weekday())]
    ru_month = month_names[datetime.datetime.today().month - 1]

    print(f"ENG:\n{eng_date}\nDaniel")
    print(f"RU:\n{ru_weekday}\n{ru_month}\nДаниель")


# 2. Вывести на экран букву "W" из символов "*"
# (звездочка).

def task_two():
    symbols = ['*\t  *\t\t*', ' *   * *   *', '  * *   * *', '   *\t *']
    for s in symbols:
        print(s)


# arithmetic

# 3. Вычислите значение
# выражения (a+4b)(a−3b)+a2 при a=2 и b=3. Ответ: -94

def task_tree(a=2, b=3):
    answer = (a + 4 * b) * (a - 3 * b) + a ** 2
    print(f"Answer: {answer}")


# 4. Пользователь вводит два числа. Найдите сумму и
# произведение данных чисел.

def task_four():
    nums = input("Enter a numbers: ").split(' ')
    print(f"Summ: {float(nums[0]) + float(nums[1])}")
    print(f"Multiple: {float(nums[0]) * float(nums[1])}")


# 5. Пользователь вводит число. Выведите на экран квадрат этого
# числа, куб этого числа.

def task_five():
    num = float(input("Enter a numbers: "))
    print(f"Square: {num ** 2}\nСube: {num ** 3}")


# 6. Пользователь вводит время в минутах и расстояние в
# километрах. Найдите скорость в м/c.

def task_six():
    time = float(input("Enter a minutes: ")) * 60
    distance = float(input("Enter a distance: ")) * 1000
    print(f"Speed: {distance / time:.5f}")


# 7. Выведите на экран прямоугольник из нулей. Количество строк
# вводит пользователь, количество столбцов равно 5.

def task_seven():
    rows = int(input("Enter a numbers: "))
    for i in range(rows):
        print("0 0 0 0 0")


# 8. Для данного n найти сумму 1+2+3+...+n. Например,
# для n=10 ответ равен 55

def task_eight():
    num = int(input("Enter a numbers: "))
    sum_for_n = 0
    for i in range(num + 1):
        sum_for_n += i
    print(f"Summ: {sum_for_n}")


# 9. Выведите на экран строки (в последней строке n звездочек):
# *
# **
# ***
# ****
# *****

def task_nine():
    num = int(input("Enter a number: "))
    for i in range(num + 1):
        print("*" * i)


# 10. Вывести на экран:
# AAAAAAAAAAAAAAAA
# ABBBBBBBBBBBBBBA
# ABBBBBBBBBBBBBBA
# ABBBBBBBBBBBBBBA
# AAAAAAAAAAAAAAAA

def task_ten():
    num = int(input("Enter a number: "))
    print("A" * num * 2)
    for i in range(num - 2):
        print("A" + "B" * (num * 2 - 2) + "A")
    print("A" * num * 2)


# 11. Вывести квадрат 7 на 7 из случайных букв.

def task_eleven(row=7, col=7):
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_alphabet += ru_alphabet.upper()

    print("ENG:")
    for i in range(row):
        for j in range(col):
            print(random.choice(string.ascii_letters), end=' ')
        print()

    print("RU:")
    for i in range(row):
        for j in range(col):
            print(random.choice(ru_alphabet), end=' ')
        print()


    # Medium

# 1. Перевернуть число
# Вводится целое число. Вывести число, обратное введенному по порядку
# составляющих его цифр. Например, введено 3425, надо вывести 5243.

def task_twelve():
    num = list(input("Enter a number: "))
    print("Reverse number: ", end='')
    for n in num[::-1]:
        print(n, end='')


# 2. Посчитать четные и нечетные цифры числа
# Определить, сколько в числе четных цифр, а сколько нечетных. Число вводится с
# клавиатуры.

def task_thirteen():
    try:
        num = int(input("Enter a number: "))
        even = odd = 0
        while num > 0:
            if (num % 10) % 2 != 0:
                odd += 1
            else:
                even += 1
            num //= 10
        print(f"Even numbers: {even}\nOdd numbers: {odd}")
    except ValueError:
        print("Invalid value, try again...")
        task_thirteen()


# 3. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух
# списков.

def task_fourteen():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_numbers = []
    for num in a:
        if (num in b) and (num not in common_numbers):
            common_numbers.append(num)
    print(common_numbers)


# 4. Выбрать из строки числа
# Дана строка, содержащая натуральные числа и слова. Необходимо сформировать
# список из чисел, содержащихся в этой строке. Например, задана строка "abc83 cde7
# 1 b 24". На выходе мы должны получить список [83, 7, 1, 24].

def task_fifteen():
    pass
    # Не придумал как сделать без регулярного выражения


# 5. Посчитать количество простых чисел
# Пользователь вводит диапазон в пределе которого необходимо посчитать все
# простые числа

def search_simp_nums():
    nums = input("Enter a numbers: ").split(' ')
    start = int(nums[0])
    end = int(nums[1])
    return simple_list(start, end)


def simple_list(start, end):
    simp_num = []
    for num in range(start, end + 1):
        k = 0
        if num == 1:
            k = 1
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                k = 1
        if k < 1:
            simp_num.append(num)
    return simp_num


# 6. Вывести таблицу умножения

def task_seventeen():
    task_seventeen_part_two(1, 5)
    task_seventeen_part_two(6, 10)


def task_seventeen_part_two(f_num, l_num):
    for i in range(1, 11):
        for j in range(f_num, l_num + 1):
            print(f"{j} x {i} = {j * i}", end='\t\t')
        print('')
    print()


# Topic "Files"

# Напишите функцию read_last(lines, file), которая будет открывать определенный
# файл file и выводить на печать построчно последние строки в количестве lines (на
# всякий случай проверим, что задано положительное целое число).

def task_eighteen():
    file_data = input("Enter the path to the file and the number of lines: \n\t").split(" ")
    try:
        read_last(file_data[0], int(file_data[1]))
    except Exception:
        print("Your enter invalid arguments!")


def read_last(lines, file_name):
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            rows = file.readlines()
            if lines > len(rows):
                lines = len(rows)
            for i in range(len(rows) - lines, len(rows)):
                print(rows[i].replace('\n', ''))
    except FileNotFoundError:
        print("Not such file or directory!")


# Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при
# помощи функции print_docs(directory).

def print_docs(directory, lvl=0):
    for i in os.listdir(directory):
        f_path = "\n" + directory + "\\" + i
        if os.path.isdir(f_path):
            print('\t' * (lvl + 1), f_path, ":")
            print_docs(f_path, lvl + 1)
        else:
            print('\t' * lvl, i)


def print_docs_var_2(directory):
    for dir_path, dir_name, files in os.walk(directory):
        print(dir_path)
        for i in dir_name:
            print(f"\t{i}")
        for i in files:
            print(f"\t{i}")


# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            word_list = (f.readlines())
        word_index = 0
        for i in range(len(word_list)):
            if len(word_list[word_index]) < len(word_list[i]):
                word_index = i
        print(search_for_similar(word_list, word_index))
    except FileNotFoundError:
        print("Not such file or directory!")


def longest_words_var_2(file):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            word_list = (f.readlines())
        w_max = max(word_list, key=len)
        print(search_for_similar(word_list, word_list.index(w_max)))
    except FileNotFoundError:
        print("Not such file or directory!")
    except ValueError:
        print("The file is empty!")


def search_for_similar(word_list, word_index):
    words = []
    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace('\n', '')
    for i in range(word_index, len(word_list)):
        if len(word_list[word_index]) == len(word_list[i]):
            words.append(word_list[i])
    return words


# Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# – Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

def row_csv(filename='rows_300.csv'):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        count = 0
        for i in range(301):
            if count == 0:
                writer.writerow(["№", "Секунда", "Миллисекунда"])
                count += 1
            else:
                sec = datetime.datetime.now().second
                m_sec = datetime.datetime.now().microsecond
                writer.writerow([i, sec, m_sec])
                time.sleep(0.01)

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(' | '.join(row))


# Hard Tasks

# Напишите функцию, которая будет принимать список чисел и возвращать
# «Boom!», если в списке встречается цифра 7. В противном случае функция
# должна вернуть «there is no 7 in the list».
def boom(num_list):
    for num in num_list:
        try:
            if int(num) == 7:
                return "BOOM!"
        except ValueError:
            continue
    else:
        return "There is no 7 in the list"


# Самое длинное слово
# Напишите функцию, которая будет находить самое длинное слово в
# предложении. Если будет найдено два и больше слов одинаковой длины,
# нужно вернуть первое из них.
def longest_word_in_string(sentence):
    word_list = sentence.split(" ")
    search_max = max(word_list, key=len)
    return search_max


# Наибольшее простое число в диапазоне
# Напишите функцию, принимающую начальное и конечное значения диапазона
# чисел и возвращающую наибольшее простое число в этом диапазоне.
def max_simple_num(start, end):
    return max(simple_list(start, end))


# Сумма диапазона чисел
# Напишите функцию, которая будет принимать начальное и конечное число в
# диапазоне чисел и возвращать сумму всех чисел этого диапазона.
def sum_range(min_num, max_num):
    return sum(range(min_num, max_num+1))


if __name__ == "__main__":
    pass
