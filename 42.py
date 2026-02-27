#check perfect number
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("It is a Perfect Number.")
else:
    print("It is not a Perfect Number.")