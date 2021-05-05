def spiralize(size, n=1):
    
    counter = 0
    incrt = 0
    while n <= size ** 2:
        return_value += n
        n += incrt
        counter += 1
        if counter == 4: 
            incrt += 2
            counter = 0 
   
    return return_value
result = spiralize(5, 2)
print(result)
