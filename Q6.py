def minimum_num(arr:list) :
    low = 0
    high = len(arr)-1
    if len(arr)==1 :
        return arr[low]
    if len(arr) == 2 : 
        return arr[low] if arr[low]<arr[high] else arr[high]
    while low<high :
        mid = (low+high)//2
        print("mid :",mid)
        if arr[mid]<arr[mid+1] and mid == 0:        # FIX THE CONDITION TOO
            return arr[mid]         # FIX FROM HERE BELOW 
        if arr[mid]<arr[mid-1] :
            return arr[mid]
        if arr[low] > arr[high] :
            high = mid+1
        else : 
            high = mid-1
    
# print(minimum_num([5, 6, 1, 2, 3, 4]))
# print(minimum_num([3,4,5,1,2]))
print(minimum_num([5,1,2,3,4]))
# print(minimum_num([2, 3, 1]))