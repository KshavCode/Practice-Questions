array = [1, 2, 4, 5, 8, 9]
target = 7

if target >= array[-1] :
    print(array[-1])
else :
    low = 0
    high = len(array)
    while low<=high :
        mid = (low+high)//2
        if array[mid]< target < array[mid+1] :
            if abs(target-array[mid]) > abs(target-array[mid+1]) :
                print(array[mid+1])
            else :
                print(array[mid])
            break
        elif array[mid-1]< target < array[mid] :
            if abs(target-array[mid-1]) > abs(target-array[mid]) :
                print(array[mid])
            else :
                print(array[mid-1])
            break
        elif array[mid]==target :
            print(array[mid])
        else :
            if target > array[mid] :
                low = mid 
            else :
                high = mid+1