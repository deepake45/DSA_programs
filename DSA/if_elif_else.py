a = int(input("Enter the average mark : "))

if a <= 100 and a > 90:
    print("grade of the student is O")

elif a <= 90 and a > 80:
    print("grade of the student is A")

elif a <= 80 and a > 70:
    print("grade of the student is B")

elif a <= 70 and a > 60:
    print("grade of the student is C")

elif a <=60 and a >= 50:
    print("grade of the student is P")

else:
    print("student is failed")
