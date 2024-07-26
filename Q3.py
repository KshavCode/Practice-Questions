string = "zxvczbtxyzvy"
occ = dict()

for i in string :
    if i not in occ :
        occ[i] = 0
    occ[i] += 1

for i in occ :
    if occ[i] == 1 :
        print(i)
        break
