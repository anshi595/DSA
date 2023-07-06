#Find First and Last Position of Element in Sorted Array (LeetCode)
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Q2: Find the number of occurence of 8 = (4-3)+1=2
def serachRange(arr: list[int], target: int)-> list[int]:
        def leftOccurnece(arr: list[int], target: int)-> int:
            low=0
            high= len(arr)-1
            mid= (low + high)//2
            ans=-1
            while(low <=high):
                if arr[mid]==target:
                    ans=mid
                    high= mid-1
                elif arr[mid] > target:
                    #left side
                    high = mid-1
                elif arr[mid] < target:
                    low= mid+1
                mid= (low + high)//2
            return ans
        
        def rightOccurnece(arr: list[int], target: int)-> int:
            low=0
            high= len(arr)-1
            mid= (low + high)//2
            ans=-1
            while(low <=high):
                if arr[mid]==target:
                    ans=mid
                    low= mid +1
                elif arr[mid] > target:
                    #left side
                    high = mid-1
                elif arr[mid] < target:
                    low= mid+1
                mid= (low + high)//2
            return ans
        return [leftOccurnece(arr, target),rightOccurnece(arr,target)]


        
arr=[5,7,7,8,8,10]
#print(serachRange(arr, 8))
#print(serachRange(arr, 7))

#Q3 Peek Index In a mountain Array(LeetCode)
#Input: arr = [0,10,5,2]
#Output: 1
def peakElement(arr: list[int])-> int:
    low=0
    high=len(arr)-1
    mid= (low + high)//2
    while(low < high):
        if arr[mid] < arr[mid+1]:
            low= mid +1
        else:
            #arr[mid] > arr[mid]+1 so move left side that is change high
            high= mid
        mid= (low + high)//2
    return low

        
arr = [0,10,5,2]
#print(f"Peak Element is at index:", peakElement(arr))

#Q4 Find Pivot in an array 
#arr=[8, 10, 17, 1, 3] o/p=pivot index at 3
def getPivot(arr):
    low=0
    high= len(arr)-1
    mid= (low + high)//2
    while(low <high):
        if arr[mid]>=arr[0]:
            #mid lies on first line (all values will be greater than arr[0])
            low= mid+1
        else:
            #mid lies on second line
            high=mid

        mid= (low + high)//2
    
    return low


inp=[8, 10, 17, 1, 3]
#print(f"The Pivot Index is at:", getPivot(inp))

#Q4 Search in rotated sorted array (LeetCode)
def search(nums: list[int], target: int) -> int:
        low=0
        high= len(nums)-1
        def getPivot(arr):
            low=0
            high= len(arr)-1
            mid= (low + high)//2
            while(low <high):
                if arr[mid]>=arr[0]:
                    
                    low= mid+1
                else:
                    #mid lies on second line
                    high=mid

                mid= (low + high)//2
            
            return low
        
        def binarySearch(arr, low, high, target):
            #low=0
            #high= len(arr)-1
            mid= (low + high)//2
            while low<=high:
                if arr[mid]==target:
                    return mid
                elif arr[mid] > target:
                    high= mid -1
                elif arr[mid] < target:
                    low= mid + 1
                mid= (low + high)//2
            return -1
        pivot=getPivot(nums)

        if target>=nums[pivot] and target<=nums[high]:
            return binarySearch(nums, pivot, high, target)
        else:
            return binarySearch(nums, low, pivot-1, target)

nums = [4,5,6,7,0,1,2]
#print(search(nums, target=0))

#Q69 Sqrt(x)
#I/P: x=4
#o/p= 2   T.C O(logN)
def sqrt(x):
    #0, 1, 2, ,3 , -------, n
    l, r = 0, x
    res = 0
    while l <= r:
        mid = (l+r) //2
        if mid*mid > x:
            r = mid - 1
        elif mid*mid < x:
            l = mid + 1
            res = mid
        else:
            return mid
    return res

print(sqrt(100))





