print("------Check type of variable.---------")
num = input("Enter anything: ")

if num.isdigit():
    num = int(num)
else:
    try:
        num = float(num)
    except:
        pass

print(type(num))