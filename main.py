# username = input ("Введите имя: ")
# if username == "Маша" :
#      print ("hi")
# elif username == "Оля" :
#      print ("olya")
# else:
#      print ("kak ty zovut?")

# n = int(input())


# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print (i, "fff")
#     elif i > n // 2:
#         print (i, n , "hhhh")
#         flag = False
#     i += 1


# Найдите сумму цифр трехзначного числа


# a = int(input("Введите трехзначное число  "  ))

# a1 = a%10
# a2 = a%100//10
# a3 = a//100

# print (a1, a2, a3)
# print (a1+a2+a3)

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# S = int(input("Всего журавликов, введите  "  ))

# if (S%6 == 0) :
#     x = S//6
#     Kat = 4*x
#     Pet_Serg = x
#     print(f"Катя сделала {Kat}, Сережа и Петя сделали по {Pet_Serg}")

# else :
#     print("Такой вариант невозможен")


# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.




# a = int(input("Введите шестизначное число  "  ))

# a1 = a%10
# a2 = a%100//10
# a3 = a%1000//100
# а4 = a%10000//1000
# а5 = a%100000//10000
# а6 = a%1000000//100000
# print(a1,a2,a3,а4,а5,а6)

# if ((a1+a2+a3) == (а4+а5+а6)):
#     print ("Ваш билет счастливый")

# else: 
#     print("Ваше билет не счастливый")
    

# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# m=int(input("vvedite m  "  ))
# n=int(input("vvedite n "))
# k=int(input("vvedite k"))

# if m%k == 0 or n//k == 0 :
#     if n*m >= k:
#         print ("ok")
#     else:
#         print ("ne ok")
# else:
#     print ("ne ok")



# fib = 0
# fib1 = 1
# fib2 = 0
# n = 9
# count = 0


# while fib2 < n:
#     fib2 = fib + fib1
#     fib = fib1
#     fib1 = fib2
#     count += 1 
#     if fib2 > n: 
#         print("-1")
#     elif fib2 == n:
#         print (count)
# print (fib2)


# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!

# list = [2, 5, 10, 7, 24, 50] 
# min = list[1]
# max = list[2]
# n = len(list)
# i = 0

# for i in range(n) :
#     if list[i] < min :
#         min = list [i]
#     else :
#         max = list[i]

# while i < n:
#     if list[i] < min :
#        min = list [i]
#     else :
#         max = list[i]
#     i = i+1
# print (min, max)


# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# list = [-20, 30, 20, -40, 50, 10, 10, 10, -10]
# count = 0
# count_max = 0
# n = len(list)
# i = 0

# for i in range(n): 
#     if list[i] >=0 and list[i+1] >= 0:
#         count = count + 1
#         if count > count_max:
#             count_max = count
#             count = 0
# print (count_max+1)

# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

# lists = 'OOOОPPPPОРОРРРРРРРРООРОРОРРРРРРРРРРРРРPPPPPPPPPPPPPPPРРРРРР'
# i = 0
# nP = 0
# nPmax = 0

#красивое решение с умножением строки

# while 'Р'*i in mon:
#     i = i + 1
# print (i)


# # решение с перебором в списке
# for list in lists :
#     if (list == "P"):
#         nP = nP + 1
#     else :
#         if nP > nPmax:
#             nPmax = nP
#         nP = 0
    
# print (nPmax)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

    

# gotovo , mozno krasivee

# list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# i = 0
# n = len(list)
# sum_ed = 0
# sum_nul = 0

# for i in range (n):
#     if list [i] == 1 :
#         sum_ed = sum_ed +1
#     else :
#         sum_nul = sum_nul +1
# i = i + 1       

# if sum_ed < sum_nul : 
#     print (sum_ed)
# else :
#     print (sum_nul)
    

# pro stepen - gotovo

# n = 22
# i = 0
# stepen = 1

# for i in range (n):
#     if n > stepen :
#         stepen = stepen * 2
#         i = i+1
# print (stepen//2)

# pro katya i petya

# p = 6
# s = 5
# x = 1
# y = 1

# вариант с флагом с семинара 

#flag = 1
# while flag and x<1000:
#     y = x    
#     while flag and y <= 1000:
#         if x + y == s and x * y == p :
#             print (x,y)
#             flag = False
#         y = y + 1
#     x = x + 1

# вариант через фор после семинара
# for x in range (1000) :
#     for y in range (1000):
#         if x + y == s and x * y == p:
#             print (x, y)
#             y = y + 1
#         x = x + 1






# ## ЛЕКЦИЯ 2

# temp = [1,2,8]
# #print(len(temp))

# #будет перебирать инднксы и элементы
# for i in range(len(temp)):
#     print (i)
#     print (temp[i])

# #будет перебирать элементы списка
# for i in temp:
#     print (i) 

#будет добавлять элементы в конец массива перебором ренже, под скрытым потом удалять последний элемент в цикле
# temp = []
# for i in range(10):
#     temp.append(i)
#     #print(temp.pop())
# print(temp.pop(3)) #удалили 3й (с нулевого) элемента и вывели его
# temp.pop(3) #удалили 3й элемент (после удаления предыдущего это 4)
# print(temp) # 0 1 2 5 6 7 8 9

# temp.insert(3,4) #добавили на 3ю позицию цифру 4
# temp.insert(3,3)
# print(temp)

# print (temp[8:2:-2]) #выведет от 8 до 2 с шагом -2

# # добавили два элемента в массив
# temps = []
# temps.append("ffffffoooo")
# temps.append("ffoo")
# print (temps)
# n=len(temps)

# for i in range(n) :
#     print (i)
#     print (temps[i])

# # # slovo = "slovo"
# # # bukva = slovo[3]
# # # print(bukva)

# # # temp = "fffooo"
# # # n = len(temp)
# # # for i in range(n):
# # #     bukva = temp [i]
# # #     print(bukva)

# # # print(temp[-5]) #выводим 5ю справа букву

#### ЛЕКЦИЯ 2 



# dictionary = {'up': '1', 'left': '2', 'down': '4'}
# print(dictionary)

# for item in dictionary :
#     print(item)

# for  (k,v) in dictionary.items():
#     print(k,v)



# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# a = set(list)
# print (len(a))
# b = []
# for i in a:
#     if not i in b:
#         b.append(i)
# print (len(b))

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# a = set(list)
# print (len(a))
# b = [i for i in b if not i in b] # генератор списков в лекции 3
# # for i in a:
# #     if not i in b:
# #         b.append(i)
# print (len(b))

## решила сама но только с крайними
# list = [1, 1, 2, 0, -1, 3, 4, 4]
# n = len(list)
# count = 0
# for i in range (n) :
#     if list [i]  == list [i-1] :
#         count = count + 1
# n = n - count
# print (n)


# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# list = [1, 2, 3, 4, 5]
# k = 3

# for i in range(k):
#     n = list.pop()
#     list.insert(0,n)
# print(list)

# # list = [1, 2, 3, 4, 5]
# # print(len(set(list)))
# # print (list[-2:]+list[:-2])
# # k = 9
# k = k % len(list)

# # # list.pop(1)
# # # print (list)
# list.remove(4)
# # # print(list)
# print(list, k)

# for i in range (k):
#     print (list)
#     x = list.pop(-1)
#     list.insert(0, x)
# print(list)


# dict1 = {(1,1,1):'222', '222':[1,1,1], 'ad': 1212, 11:12}
# for i in dict1 :
#     print (i, dict1[i])

# for i in dict1.values():
#    print(i)
#for i,j in dict1.items():
#   print(i, j)

#ключ и значение жи

# dict1[n] #


### Задача 2: Найти максимально близкий элемент

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

# min = abs(list_1[0] - k)
 
# for i in range(len(list_1)):
#     a1 = abs(list_1[i] - k)
#     if a1 <= min: 
#         min = a1
#         max = list_1[i]

# print(max)

#Задача про подсчет очков введенногоо слова

# sum = 0
# k = "АiiiSRRRqqDDDDDDD"
# k = k.upper()

# dict1 = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т", "A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
# dict2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
# dict3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
# dict4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
# dict5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
# dict6 = ['J','X', 'Ш', 'Э', 'Ю']
# dict7 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

# for i in range(len(k)):
#     if k[i] in dict1:
#         sum = sum + 1
#     if k[i] in dict2:
#         sum = sum + 2
#     if k[i] in dict3:
#         sum = sum + 3
#     if k[i] in dict4:
#         sum = sum + 4
#     if k[i] in dict5:
#         sum = sum + 5
#     if k[i] in dict6:
#         sum = sum + 8
#     if k[i] in dict7:
#         sum = sum + 10

# print(sum)


## Скрэмбл. Вариант решения 2.

# dict_rez = {
#             "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
#             "D": 2, "G": 2,
#             "B": 3, "C": 3, "M": 3, "P": 3,
#             "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
#             "K": 5,
#             "J": 8, "X": 8,
#             "Q": 10, "Z": 10,
#             "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1,
#             "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
#             "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
#             "Й": 4, "Ы": 4,
#             "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
#             "Ш": 8, "Э": 8, "Ю": 8,
#             "Ф": 10, "Щ": 10, "Ъ": 10
# }

# for i in range(len(k)):
#     if k[i] in dict_rez:
#         sum = sum + dict_rez.get(k[i], 0)
    
# print(sum)



# ###ЛЕКЦИЯ 3 ФУНКЦИИ

# def summa_int (*int):
#     res = 0
#     for i in int:
#         res = res + i
#     return (res)

# print (summa_int(1, 3))

# def summa_str (*args):
#     res = ''
#     for i in args:
#         res = res + i
#     return (res)

# print (summa_str('s', 'sd'))

# import modul1
# print(modul1.max(5,8))

# from modul1 import max #или поставить *, чтоб импортировать все функции из данного модуля
# print(max(8,99))

# import modul1 as m1 #для действий в этом файле 
# print(m1.max(5,8))