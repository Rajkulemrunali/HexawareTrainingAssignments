def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    print("Bubble Sort :     ",arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
    
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
def merge_sort(arr,left,right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right) 
    return arr    
   

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1    
    
def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
    return arr
        
def linear_search(arr,key):
    n=len(arr)
    for i in range(0, n):
        if (arr[i] == key):
            return i
    return -1        

        
def binary_search(arr,low,high,key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

arr=[6,3,7,2,8,1]
key=6
print("Unsorted Array :  ", arr)
def sort(ch):
    if(ch==1):
        bubble_sort(arr)
    elif(ch==2):
        print("Insertion Sort:   ",insertion_sort(arr))
    elif(ch==3):
        print("Selection Sort:   ",selection_sort(arr))
    elif(ch==4):
        print("Merge Sort:       ",merge_sort(arr,0,len(arr)-1))
    elif(ch==5):
        print("Quick Sort:       ",quick_sort(arr,0,len(arr)-1))
    
def search(ch):    
    if(ch==1):
        result=linear_search(arr,key)
        print("Searching through linear Search...")
        if (result == -1):
            print("Element Not Present In Array")
        else:
            print("Element Present At Index", result)
    elif(ch==2):
        result=binary_search(arr,0,len(arr)-1,key)
        print("Searching through Binary Search...")
        if result != -1:
            print("Element Present At Index", result)
        else:
            print("Element Not Present In Array")


#Driving Code : Instructions
"""
sort 1:bubble_sort
sort 2:insertion_sort
sort 3:selection_sort
sort 4:merge_sort
sort 5:quick_sort

search 1:linear search
search 2:binary search
"""
sort(1)
sort(2)
sort(3)
sort(4)
sort(5)
search(1)
search(2)
