from random import randint
fToSort = open("tosort.txt", "w")

i = 1
print("введите нужное кол-во случайных чисел")
m = int(input())

while i <= m:
    fToSort.write(str(randint(0, 10000000000)))
    fToSort.write(" ")
    i = i + 1