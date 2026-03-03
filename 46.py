def print_numbers(n):
    if n == 0:          # Base condition
        return 0
    
    print_numbers(n-1)  # Recursive call
    print(n)            # Print after recursive call
print_numbers(5)