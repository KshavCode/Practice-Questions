def fun1(nums:list, n:int, target:int)->list :
    start = -1
    end = -1
    for i in range(n) :
        if target == nums[i] :
            start = i
            end = i
            while nums[end] == target :
                end += 1
                if len(nums) == end :
                    break
            break
    if end == - 1 :
        return [start, end]     
    return [start, end-1]     

# Using Two Pointer
def fun2(nums:list, target:int) -> list : 
    low = 0
    high = len(nums)-1
    while low<=high : 
        if nums[low] != target :
            low += 1
        if nums[high] != target :
            high -= 1
        if nums[low]==nums[high]==target:
            return [low, high]
    return [-1, -1]
            
        


num_list = [2,4,5,5,5,5,5,8,9,12]
n = 10
print(fun1(num_list, 10, 5))
print(fun2(num_list, 5))


