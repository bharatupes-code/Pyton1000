# Open file
file = open("name.txt", "r")

names = file.readlines()

total_names = 0
vowel_count = 0
longest_name = ""

vowels = "aeiouAEIOU"

for name in names:
    name = name.strip()
    total_names += 1

    # Check vowel
    if name[0] in vowels:
        vowel_count += 1

    # Check longest
    if len(name) > len(longest_name):
        longest_name = name

file.close()

print("Total names:", total_names)
print("Names starting with vowel:", vowel_count)
print("Longest name:", longest_name)