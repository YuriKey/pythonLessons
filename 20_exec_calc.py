# Напишите проект "Калькулятор".
# Инструкции к заданию:
# Напишите скрипт "калькулятор", который будет принимать от
# пользователя на вход:
# 1-е число
# арифметический знак, один из: +, -, *, /
# 2-е число
# производить сложение, вычитание, умножение или деление,
# в зависимости от введенного знака
# А так же предусмотрите проверку на то, что на ноль
# делить нельзя. И другие виды некорректно введенных данных.
# Данное задание Вам необходимо выполнить самостоятельно и
# стараться не пользоваться сторонними источниками
# Ответ в виде текста, прошу приложить в Решения или
# прислать на почту aleksandr_stepik@mail.ru

# def value_verification(x, y, z):
#     if type(int(x)) == int:
#         x = x
#         if y == '+' or y == '-' or y == '*' or y == '/':
#             y = y
#             if type(int(z)) == int:
#                 z = z
#             else:
#                 print('Второе число некорректно. Начните заново.')
#         else:
#             print('Введенное действие некорректно. Начните заново.')
#     else:
#         print('Первое число некорректно. Начните заново.')
#     return x, y, z
def action(m, n, k):
    if n == '+':
        print('Результат действия: ' + str(m + k))
    elif n == '-':
        print('Результат действия: ' + str(m - k))
    elif n == '*':
        print('Результат действия: ' + str(m * k))
    elif n == '/':
        try:
            result = (m / k)
            print('Результат действия: ' + str(int(m / k)))
        except ZeroDivisionError:
            result = 0
            print("На ноль делить нельзя.")
    else:
        print('Введите корректный символ действия.')


try:
    a = int(input('Введите первое число: '))
    b = input('Введите действие +, -, * или /: ')
    c = int(input('Введите второе число: '))
    action(a, b, c)
except ValueError:
    print('Число введено не верно. Повторите попытку.')