text=input("Enter a string:")
vowels=('a','e','i','o','u')
count=0
for ch in text:
    if ch in vowels:
        count+=1
print("Number of vowels in string is ",count)