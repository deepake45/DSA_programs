"""question 1
Bubble sort"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
a = int(input("Enter the no of elements of the array : "))
arr = []
for i in range(a):
        b = int(input("Enter the elements of the array : "))
        arr.append(b)
print("original list : ", arr)
sorted_array = bubble_sort(arr)
print("Sorted array : ", sorted_array)
