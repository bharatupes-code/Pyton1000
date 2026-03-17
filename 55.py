T = (1, 2, 3)
T[2] = 4     # Error!
print(T)         
T = T[:2] + (4,)     # OK: (1, 2, 4)
print(T)