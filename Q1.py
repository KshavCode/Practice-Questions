array = [1, 1, 0, 1, 1, 1]
newlis = []
c = 0 
highest = 0
for i in range(len(array)) :
    if array[i] == 1 :
            c += 1
            if c > highest : 
                highest = c
    else : 
        c = 0
        
print(highest)