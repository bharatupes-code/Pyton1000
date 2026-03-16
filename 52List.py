T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T) # Make a list from a tuple's items
tmp.sort()# Sort the list
print(tmp)

T = tuple(tmp) # Make a tuple from the list's items
print(T)


