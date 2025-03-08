def same_or_not(arr1:list, arr2:list) :
    if len(arr1) != len(arr2) : 
        return False 
    return list(sorted(arr1)) == list(sorted(arr2))
    
    
print(same_or_not([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))