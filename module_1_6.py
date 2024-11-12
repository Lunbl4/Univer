'''

lesson 232

Практическое задание по теме: "Словари и множества"

Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.
2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.

Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.

3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.

'''

my_dict = {'Qwe' : 2001, 'Asd' : 2002, 'Zxc' : 2003}
print(my_dict)
print(my_dict['Qwe'])
print(my_dict.get('Rty')) # пытаемся вывести пару по несуществующему ключу
my_dict.update({'Wewewe' : 2004,
                'Dfgnng' : 2005
                })
print(my_dict.pop('Asd')) # значение удалённой пары
print(my_dict)


my_set = {'slovo', 123, 2.5, 123, (324234, 123), 123}
print(my_set)
my_set.update([7689,"hgjk"])
my_set.remove(123)
print(my_set)