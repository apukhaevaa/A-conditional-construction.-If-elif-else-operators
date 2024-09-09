# Пухаева Алина Александровна
# A conditional construction. If, elif, else operators.
# 09.09.2024
# Notes: ctrl+alt+L
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print(int(3))
elif first == second or first == third or second == third:
    print(2)
else:
    print(int(0))