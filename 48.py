def find_max_min():
    file = open("numbers.txt", "r")   
    data = file.read()                
    file.close()                      
    numbers = data.split()           
    max_num = int(numbers[0])         
    min_num = int(numbers[0])         
    for n in numbers:
        num = int(n)
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print("Maximum number:", max_num)
    print("Minimum number:", min_num)

find_max_min()