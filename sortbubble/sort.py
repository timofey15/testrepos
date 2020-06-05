fToSort = open("sorting.txt", "r")
fSorted = open("sorting new.txt", "w")

array = fToSort.read().split()

count = len(array)

a = [int(elem) for elem in array]

i = 0
int(i)
j = 1
int(j)
to_change = 0
int(to_change)


for p in range(count):
    z = 0
    print(z)
    print(a)
    while z < (count - p - 1):
        if a[z] > a[z + 1]:
            to_change = a[z + 1]
            a[z + 1] = a[z]
            a[z] = to_change
        z = z + 1
        print(a)
    p = p + 1
for element in a:
    fSorted.write(str(element))
    fSorted.write(" ")

fToSort.close()
fSorted.close()