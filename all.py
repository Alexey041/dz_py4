#1
""" Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """

some_str = input('Введите число: ').split(',')  
num = int(some_str[1])
count = 0
while num > 0:
    num = num // 10
    count += 1

import math
print(round(math.pi, count))

#2
""" Задайте натуральное число N. Напишите программу, которая составит список простых
множителей числа N. """

num = int(input('Введите натуральное число: '))
multipliers_list = []
result_list = [1]
for i in range(1, num + 1):
    if num % i == 0:
        multipliers_list.append(i)

for i in multipliers_list:
    count = 0
    for index in range(1, i + 1):
        if i % index == 0:
            count += 1
            if index == i:
                if count == 2:
                    result_list.append(index)

print(result_list)

#3
""" Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности. """

some_list = list(map(float, input('Введите последовательность чисел через \
пробел: ').split()))

for i in some_list:
    count = 0
    for index in some_list:
        if index == i:
            count += 1
            if count > 1:
                some_list.remove(index)


print(some_list)
