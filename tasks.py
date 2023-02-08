import datetime
import random
import string


# information output


def task_one():
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август",
                   "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

    eng_date = datetime.datetime.now().strftime('%A\n%B')

    ru_weekday = weekdays[int(datetime.datetime.today().weekday())]
    ru_month = month_names[datetime.datetime.today().month - 1]

    print(f"ENG:\n{eng_date}\nDaniel")
    print(f"RU:\n{ru_weekday}\n{ru_month}\nДаниель")


def task_two():
    symbols = ['*\t  *\t\t*', ' *   * *   *', '  * *   * *', '   *\t *']
    for s in symbols:
        print(s)


# arithmetic

def task_tree(a=2, b=3):
    answer = (a + 4 * b) * (a - 3 * b) + a ** 2
    print(f"Answer: {answer}")


def task_four():
    nums = input("Enter a numbers: ").split(' ')
    print(f"Summ: {float(nums[0]) + float(nums[1])}")
    print(f"Multiple: {float(nums[0]) * float(nums[1])}")


def task_five():
    num = float(input("Enter a numbers: "))
    print(f"Square: {num ** 2}\nСube: {num ** 3}")


def task_six():
    time = float(input("Enter a minutes: ")) * 60
    distance = float(input("Enter a distance: ")) * 1000
    print(f"Speed: {distance / time:.5f}")


def task_seven():
    rows = int(input("Enter a numbers: "))
    for i in range(rows):
        print("0 0 0 0 0")


def task_eight():
    num = int(input("Enter a numbers: "))
    sum_for_n = 0
    for i in range(num + 1):
        sum_for_n += i
    print(f"Summ: {sum_for_n}")


def task_nine():
    num = int(input("Enter a number: "))
    for i in range(num + 1):
        print("*" * i)


def task_ten():
    num = int(input("Enter a number: "))
    print("A" * num * 2)
    for i in range(num - 2):
        print("A" + "B" * (num * 2 - 2) + "A")
    print("A" * num * 2)


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


def task_twelve():
    num = list(input("Enter a number: "))
    print("Reverse number: ", end='')
    for n in num[::-1]:
        print(n, end='')


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


def task_fourteen():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_numbers = []
    for num in a:
        if (num in b) and (num not in common_numbers):
            common_numbers.append(num)
    print(common_numbers)


def task_fifteen():
    pass


def task_sixteen():
    nums = input("Enter a numbers: ").split(' ')
    simp_num = []
    start = int(nums[0])
    end = int(nums[1])
    for i in range(start, end + 1):
        k = 0
        if i == 1:
            k = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                k = 1
        if k < 1:
            simp_num.append(i)

    print(simp_num)


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


if __name__ == "__main__":
    task_eighteen()
