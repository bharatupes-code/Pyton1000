text=input("Enter a string:")
count=0
for ch in text:
    if ch.isupper():
        count+=1
        print("Number of capital letter is :",count)