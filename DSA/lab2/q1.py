"""question 3"""

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
n = int(input("Enter no of elements : "))
arr = []
for i in range(n):
    a = int(input("enter the elements of the array : "))
    arr.append(a)
key = int(input("Enter the element to search : "))
result = linear_search(arr, key)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
