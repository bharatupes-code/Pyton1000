#check palindrome string
text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("It is a palindrome string.")
else:
    print("It is not a palindrome string.")