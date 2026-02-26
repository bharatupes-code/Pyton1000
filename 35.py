# Check triangle type.
a=int(input("Enter a side of a triangle:"))
b=int(input("Enter b side of a triangle:"))
c=int(input("Enter c side of a trangle:"))
if a==b==c:
    print("It is a equilateral traingle")
elif a==b or b==c or c==a:
    print("It is a isoceles triangle")
else:
    print("It is a scalene triangle")