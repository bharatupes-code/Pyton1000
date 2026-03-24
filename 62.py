s = input("Enter string: ")

s = s.lower()   # convert to lowercase
count = {}

for ch in s:
    if ch.isalpha():   # check if character is alphabet
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

for key in sorted(count):
    print(key, ":", count[key])


