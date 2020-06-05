import sys
fToCheck = open("sorted.txt", "r")

a = fToCheck.read().split()

count = len(a)

checkList = [int(elem) for elem in a]

i = 0
int(i)
j = i + 1
int(j)

for i in range(count - 1):
    if checkList[i] > checkList[j]:
        print("отсортированно неправильно!")
        sys.exit()
    i = i + 1
    j = j + 1
print("отсортированно правильно!")

fToCheck.close()