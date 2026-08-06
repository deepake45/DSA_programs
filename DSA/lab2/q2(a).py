""" question 2(sorted array)"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high :
        mid = (low + high ) // 2
        if arr[mid] == key:
             return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
n  = int(input("Enter no of elements : "))
arr = []
for i in range(n):
    a = int(input("Enter the elements of the array : "))
    arr.append(a)
key = int(input("Enter the elements to search : "))
result = binary_search(arr, key)
if result != -1:
    print("Element found at the index : ",result)
else:
    print("Element is not found")
