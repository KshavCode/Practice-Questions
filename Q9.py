arr = [10, 3, 5, 6, 2]
prod = []

for i in range(len(arr)) :
    res = 1
    for j in range(len(arr)) :
        if i != j :
            res *= arr[j]
    prod.append(res)

print(prod)