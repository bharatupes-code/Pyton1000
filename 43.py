#check strong number
num = int(input("Enter a number: "))
original = num
sum_factorial = 0

while num > 0:
    digit = num % 10
    
    # Find factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
        
    sum_factorial += fact
    num = num // 10

if sum_factorial == original:
    print("It is a Strong Number.")
else:
    print("It is not a Strong Number.")