""" question 2
insertion sort"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j =i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
a = int(input("Enter the no of elements of the array : "))
arr = []
for k in range(a):
    b = int(input("Enter the elements of the array : "))
    arr.append(b)
print("Original array : ", arr)
sorted_array = insertion_sort(arr)
print("Sorted array : ", sorted_array)
