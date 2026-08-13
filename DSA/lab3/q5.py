"""question 5
quick sort"""

def quick_sort(a, low, high):
    if low < high:
        pivot = a[low]
        i = low + 1
        j = high
        while True:
            while i <= high and a[i] <= pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
            else:
                break
        a[low], a[j] = a[j], a[low]
        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)
    return a
n = int(input("Enter the no of elements of the array: "))
a = []
for k in range(n):
    b = int(input("Enter the elements of the array: "))
    a.append(b)
print("Original List:", a)
sorted_array = quick_sort(a, 0, n - 1)
print("Sorted Array:", sorted_array)
