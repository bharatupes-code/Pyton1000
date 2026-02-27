#Check Armstrong number.
num = int(input("Enter a number: "))
original = num
sum_of_powers = 0

# Count number of digits
n = len(str(num))

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** n
    num = num // 10

if sum_of_powers == original:
    print("It is an Armstrong Number.")
else:
    print("It is not an Armstrong Number.")