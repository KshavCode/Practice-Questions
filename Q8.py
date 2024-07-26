array = [1, 2, 3, 6, 3, 6, 1]
numberocc = dict()

for i in range(len(array)) :
    if array[i] not in numberocc :
        numberocc[i] = 0
    numberocc[i] += 1

for i in numberocc :
    if numberocc[i] > 1 :
        print(i)