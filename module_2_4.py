'''

lesson/250

Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

Ваша задача:
Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.

Задача "Всё не так уж просто":

Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).

Пункты задачи:

Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от
значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).


Пример результата выполнения программы:

Исходный код:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Вывод на консоль:

Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]


'''

# Дано
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # СПИСОК

# Решение
is_prime = True # не придумал куда или как вставить :), в роли переключателя

primes = [] # простые числа, которые делятся на 1 и на себя, без остатка
not_primes = [] # непростые числа, делятся на 2,3,5

for number in numbers:                # для любого ЧИСЛА из СПИСКА
    for i in range(2, number+1):        # для любого числа из диапазона с 2 по ЧИСЛО(не включая его)

# Выключаю проверку, т.к. в range начнём с цифры 2
#       if number == 1:                     # исключаем 1, т.к. оно ни простое, ни составное
#           print("число равно 1")
#           break

       if number == 2:                   # если число 2 - добавляем его в простые
           print("число равно 2")
           primes.append(number)
           break

       elif number % i != 0:            # если не делится ни на какое число без остатка, значит number - простое число
           primes.append(number)
           break

       elif number % i == 0:          # если число делится на что-то, значит number - СОСТАВНОЕ
           not_primes.append(number)
           break

# Итог


print("Primes: [2, 3, 5, 7, 11, 13]")
print("Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]")
print("У МЕНЯ:")
print(primes)
print(not_primes)
