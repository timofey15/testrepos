fToSort = open('tosort.txt', 'r')
fSorted = open('sorted.txt', 'w')

array = fToSort.read().split()

a = [int(elem) for elem in array]

a.sort()

for elem in a:
    fSorted.write(str(elem))
    fSorted.write(' ')

fSorted.close()