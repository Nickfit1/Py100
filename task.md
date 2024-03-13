# Изменяемые и неизменяемые типы данных в Python

## Цель урока
Научитесь различать изменяемые и неизменяемые типы данных в языке программирования Python.  
Вы изучите основные различия между этими типами данных и узнаете, какие операции допустимы для изменяемых и неизменяемых объектов.

## Теория
Типы данных в Python можно разделить на **изменяемые** и **неизменяемые**.  
Вот некоторые примеры таких типов данных:

| Изменяемые типы данных | Неизменяемые типы данных |
|-----------------------|------------------------|
| Списки                | Числа (int, float)      |
| Словари               | Строки                 |
| Множества             | Кортежи                |

Изменяемые типы данных позволяют изменять свое состояние, добавлять, удалять или изменять элементы, в то время как неизменяемые типы данных остаются неизменными после создания.  
Неизменяемые объекты не могут быть изменены непосредственно, но вы можете создать новый объект, используя исходный объект и применяя различные операции.

### Примеры изменения данных:
Изменяемый тип данных (список):
```python
my_list = [1, 2, 3, 4]
my_list[0] = 10  # заменили элемент стоящий в списке на первом месте
print(my_list)  # Вывод: [10, 2, 3, 4]
```

Неизменяемый тип данных (строка):
```python
my_string = "Hello"
new_string = "J" + my_string[1:]  # Замена первой буквы на "J"
print(new_string)  # Вывод: "Jello"
```

## Задание: Исправление опечатки
### Описание
Вы получили список названий фруктов, но в одном из слов была допущена опечатка.  
Ваша задача — исправить эту ошибку, заменив первую букву в слове.

### Задача
1. Создайте список слов: `fruits = ["яблоко", "банан", "опельсин", "виноград"]`.
2. Используя конкатенацию строк и срезы, исправьте опечатку в слове "опельсин", заменив первую букву "о" на "а".
3. Выведите исправленный список фруктов на экран.