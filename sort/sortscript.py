fToSort = open("sorting.txt", "r")
fSorting = open("sorting new.txt", "w")


a = fToSort.read().split()

count = len(a)

array = [int(elem) for elem in a]

i = 0
int(i)
j = i + 1
int(j)
n=0
int(n)

for i in range(count):
    minimal = array[i]
    n = i
    j = i
    while j < count:
        if minimal > array[j]:
            minimal = array[j]
            n = j
        j = j + 1
    array[n] = array[i]
    array[i] = minimal
    i += 1

for element in array:
    fSorting.write(str(element))
    fSorting.write(' ')

fToSort.close()
fSorting.close()



