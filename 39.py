#check centuary year
year = int(input("Enter a year: "))

if year % 100 == 0:
    print("It is a century year.")
else:
    print("It is not a century year.")