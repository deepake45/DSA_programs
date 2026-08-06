"""question 2(array is not sorted)"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)// 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid +1
        else:
            high = mid - 1
    return -1
n = int(input("Enter the no of elements of the array : "))
arr = []
for i in range(n):
    a = int(input("Enter the elements of the array : "))
    arr.append(a)
key = int(input("Enter the element to search : "))
if arr == sorted(arr):
    print("The input list is already sorted")
else:
    print("The input list is not sorted")
    print("Sorting the element")
    arr.sort()
print("Sorted List : ", arr)
result = binary_search(arr, key)
if result != -1:
    print("Element found at the index : ",result)
else:
    print("Element not found")
