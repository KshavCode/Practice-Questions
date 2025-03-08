def largest_k(array:list, k:int)->int :
    array = list(sorted(array))
    return array[k*-1]
                


arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
print(largest_k(arr, k))