"question 3"

def search(emp_list, key, index):
    if index == len(emp_list):
        return False
    if emp_list[index] == key:
        return True
    return search(emp_list, key, index +1)
emp_list = [1000, 1001, 1002, 1003, 1004]
key = int(input("Enter employee to search"))

if search(emp_list, key, 0):
    print("Employee ID found")
else:
    print("Employee ID not found")
