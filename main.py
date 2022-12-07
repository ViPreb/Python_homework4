# A. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
#
# n = int(input('Введите степень многочлена: '))
# a = ' '
# for k in range(n, -1, -1):
#     a += f'{random.randint(0, 100)}*x**{k} + '
# c = str(random.randint(0, 100))
# itog = str('= 0')
# print(f'{a}{c}{itog}')
# polynomial_one = a + c + itog
# f = open('text1.txt', 'w')  # изменить на text2.txt и запустить ещё раз для записи многочлена во второй файл
# for index in polynomial_one:
#     f.write(index)
# f.close()


# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re
import itertools


file1 = 'text1.txt'
file2 = 'text2.txt'
file_sum = 'text3_itog.txt'
#Получение данных из файла
def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


# Получение списка кортежей каждого (коэффициент, степень)
def convert_pol(pol):
    pol = pol.replace('= 0', '')                 # уберем символ =0
    # print (pol)
    pol = re.sub("[*]", " ", pol).split('+')    # заменим все символы * на пробел и разобьем по +
    # print(pol)
    pol = [char.split(' ') for char in pol]  # разобьем на подсписки
    # print(pol)
    pol = [[x for x in list if x] for list in pol]  # очищаем список
    # print(pol)
    for i in pol:   # проверка списка на коэффициенты, чтобы все справа и слева от х были проставлены 1, если там ничего нет
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]  # делаем словарь из списка
    # print(pol)
    return pol

# Получение списка кортежей суммы

def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    print(x)
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    # print(res)
    res.sort(key = lambda r: r[1], reverse = True)
    # print(res)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol) # составляем список из символов
    # print(var)
    coefs = [x[0] for x in pol] #из словаря берем коэффициент
    # print(coefs)
    degrees = [x[1] for x in pol] # из словаря берем степени
    # print(degrees)
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))] # соединяем в список
    # print(new_pol)
    for x in new_pol: #проверяем на 0 и 1, и обязательно учитываем, что x^0=1
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    print(new_pol)
    new_pol = list(itertools.chain(*new_pol))
    print(new_pol)
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(f'Первый   многочлен {pol1}')
print(f'Первый   многочлен {pol2}')
print(f'Итоговый многочлен {pol_sum}')




