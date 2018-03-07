def triangle_check(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print("Można stworzyć trójkąt.")
    else:
        print("Nie można stworzyć trójkąta.")

a = float(input("Podaj boki trójkąta:"))
b = float(input("Podaj boki trójkąta:"))
c = float(input("Podaj boki trójkąta:"))

triangle_check(a, b, c)
