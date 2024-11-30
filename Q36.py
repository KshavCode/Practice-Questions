class Solution:
    def rotation(self, arr:list) :
        lowest = arr[0]
        lowest_index = arr[0]
        if arr[0]<arr[-1] :
            return 0
        for i in range(1, len(arr)) :
            if lowest > arr[i] :
                lowest = arr[i]
                lowest_index = i
        return lowest_index
            
        

    def search(self, nums: list, target: int) -> int :
        low = 0
        high = len(nums)
        n = self.rotation(nums)
        arr = nums[n:]+nums[:n]
        if target > arr[-1] or target < arr[0] :
            return -1
        while low<=high :
            mid = (low+high)//2
            if arr[mid] == target :
                return (mid+n)%len(arr) 
            elif arr[mid] > target :
                high = mid - 1
            else :
                low = mid + 1
        return -1