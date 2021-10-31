from unittest import result

import matplotlib.pyplot as plt


def count_cluster(x, function):
    result = []
    if function[0] <= x <= function[3]:
        if function[0] <= x <= function[1]:
            result.append(1 - (function[1] - x) / (function[1] - function[0]))
    if function[1] <= x <= function[2]:
        result.append(1)
    if function[2] <= x <= function[3]:
        result.append(1 - (x - function[2]) / (function[3] - function[2]))
    else:
        result.append(0)
    return result

#3 трапеции, изменить значения,   массив с длительностью(вместо вводимого числа) 1 колонка-четкое значение, 2-быстрое, 3-долгое,
# графически отобразить объединение графиков нечеткого множества быстрого и долгого
def clustering(x):
    result = []
    print(f"Это на {count_cluster(x, [1, 4, 5, 8])} быстрый перелет")
    print(f"Это на {count_cluster(x, [3, 7, 7, 10])} средний перелет")
    print(f"Это на {count_cluster(x, [10, 22, 22, 25])} долгий перелет")

    result.append(count_cluster(x, [1, 4, 5, 8]))
    result.append(count_cluster(x, [10, 22, 22, 25]))

    print(result)
#максимум для одного четкого значения, среди его степеней принадлежности
    max = result[0]
    for i in result:
        if i > i:####
            max = i

    print(max)
   # plt.plot(max)#выводит заданное число(???)
   # plt.show()
    function = [1, 4, 5, 1]
    function2 = [3, 7, 7, 3]
    function3 = [10, 22, 22, 10]

    plt.plot(function)
    plt.plot(function2)
    plt.plot(function3)
    plt.show()

while True:
    clustering(int(input("Введите длительность перелета ")))

