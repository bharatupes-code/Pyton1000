#Check vowel or consonant
character=input("Enter a character:")
character=character.lower()
if len(character)!=1:
    print("Please enter single character:")
elif not character.isalpha():
    print("Enter valid alphabet only:")
elif character in ["a","e","i","o","u"]:
    print("It is vowel")
else:
    print("It is a constant")