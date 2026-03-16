J = ['abc', 'ABD', 'aBe']
J.sort() # Sort with mixed case
print(J)

K = ['abc', 'ABD', 'aBe']
K.sort(key=str.lower) # Normalize to lowercase
print(K)


L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # Change sort order
print(L)
