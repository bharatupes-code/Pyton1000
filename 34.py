#Check grade based on marks.
num=float(input("Enter your marks to see how much you grade"))
if num>=85:
    print("You obtained O+ grade")
elif num>=75 and num<85:
    print("You obtained A+ grade")
elif num>=65 and num<75:
    print("You obtained A grade")
elif num>=55 and num<65:
    print("You obtained B+ grade")
elif num>=35 and num<55:
    print("You obtained A grade")
elif num>=1 and num<35:
    print("You obtained A grade")