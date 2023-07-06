#Selection sort: select the smallest element and swap it to the left.
#T.C. O(N^2)   Best case = O(N^2) Worst Case= O(N^2)
#S.C - O(1)
# Use Case : Used for small sized array


def selection_sort(arr):
    n= len(arr)
    for i in range(0, n):
        min_index=i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index= j
        #swap the minm element with first element
        arr[i], arr[min_index]= arr[min_index], arr[i]
    return arr

#Bubble_sort: swap the adjacent element if they are in wrong order. (n-1) iteration for a n size array.
#after ith round ith largest element will be at ith rightmost position.
#T.C: O(N^2)  Worst.Case=O(N^2)   Best Case=O(N) aarray is already sorted
#S.C= O(1)


def bubble_sort(arr):
    n= len(arr)
    for i in range(0, n):
        swapped =False
        for j in range(0, n-i-1):
            #last i elements are already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped=True
        
        if swapped==False:
            #if array is already sorted
            break
            
    return arr

#Inserstion Sort: assume 1st element is sorted then start from next element, compare,  if greater shift  and copy
#T.C: O(N^2) Best Case : O(N) W.C: O(N^2)
#S.C: O(N)
#Use case: stable and in place. Adaptive for data set which are partially sorted.
def insertion_sort(arr):
    n= len(arr)
    for i in range(1, n):
        temp=arr[i]
        j= i-1
        while(j>=0):
            if arr[j] > temp:
                arr[j+1]= arr[j]
            else:
                break
            j-=1
        arr[j+1]=temp
    return arr
            
#Merge Sort: 
#T.C: O(nlogn)
#S.C: O(n)
#Usecase: Suitable for large datasets, stable and efficient.
def mergeArray(left, right):
    result=[]
    #counter for both subaarays
    left_index=0
    right_index=0
    while(left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index +=1
        else:
            result.append(right[right_index])
            right_index +=1
    while left_index < len(left):
        result.append(left[left_index])
        left_index+=1
    while right_index < len(right):
        result.append(right[right_index])
        right_index+=1
    
    return result

def mergeSort(arr):
    #base case
    if len(arr)<=1:
        return arr
    
    mid= (len(arr))//2
    #sort left part
    left=mergeSort(arr[:mid])
    #sort right part
    right=mergeSort(arr[mid:])
    #merge the sorted subarrays left and right
    return mergeArray(left, right)

#Quick Sort using last element as pivot:
#TC: O(nlogn) in best and average case and O(n^2) in worst case 
#But worst case can be avoided by using randamised pivot
#S.C: avg case= O(logn), worst case= O(n)

def partition(arr, low, high):
    pivot=arr[high]
    pivotIndex=low
    for i in range(low, high):
        if arr[i] <=pivot:
            #swap the elements 
            arr[i], arr[pivotIndex]=arr[pivotIndex], arr[i]
            pivotIndex +=1
    
    arr[pivotIndex], arr[high]=arr[high], arr[pivotIndex]
    
    return pivotIndex
        


def quickSort(arr, low, high):
    if low < high:
        pivot= partition(arr, low, high)
        #sort left part
        quickSort(arr, low, pivot-1)
        #sort right part
        quickSort(arr, pivot, high)
    return arr


    


            



array = [64, 25, 12, 22, 11]
array2=[1, 2, 3, 4, 5]
#print(f"Sorted array is :", selection_sort(array))
#print(f"Sorted array is :", bubble_sort(array))
print(f"Sorted  array is using insertion sort is  :", insertion_sort(array))
#print(f"Sorted Merged array is :", mergeSort(array))
print(f"Sorted QuickSort array is :", quickSort(array, 0, len(array)-1))




    