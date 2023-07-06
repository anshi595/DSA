#it follows brute force algorithm
#O(n)
#on both sorted and sorted
def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i]== item:
            return i
    
        
    return "Doesn't exist"

#O(logn) for binary search
#only for sorted array
def binary_search_normal(arr, item):
    low= 0
    high= len(arr)-1
    mid= (low + high)//2
    #Incase of low as 2^31-1 and high as 2^31 -1 mid will give an error to resolve it take  
    # mid = low + (high -low)/2
    while low<=high:
        if arr[mid]==item:
            return mid
        elif arr[mid] > item:
            #search in left side. change high as mid
            high= mid -1
        elif arr[mid] < item:
            #search in right side. Change mid as low
            low= mid + 1
        mid= (low + high)//2
    return -1

def binary_search_recurs(arr, low, high, item):
    if low <= high:
        mid= (low + high)//2
        if arr[mid]==item:
            return mid
        elif arr[mid]> item:
            return binary_search_recurs(arr, low, mid-1, item)
        else:
            return binary_search_recurs(arr, mid+1, high, item)

    else:
        return -1

    
    


arr=[12, 34, 45, 78]
#print(linear_search(arr, 55))
arr2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_recurs(arr2, 0, len(arr2)-1, 9))
arr3= [2, 4, 6, 8, 12, 16]
print(f"The Index is :" , binary_search_normal(arr2, 4))


