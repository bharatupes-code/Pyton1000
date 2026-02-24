#Create simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("SELECT OPERATION")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("Enter choice(1/2/3/4):")
if choice == "1":
    print("Addition:",num1+num2)
elif choice == "2":
    print("Subtraction:",num1-num2)
elif choice == "3":
    print("Multiplication:",num1*num2)
elif choice== "4":
    if num2!=0:
     print("Divison:",num1/num2)
    else:
     print("Division is not possible")
else:
    print("INvalid choice")
print("-----Thank You for using my calculator-------")

