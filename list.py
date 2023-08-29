def even_numbers(min,max ):
    evenNumbers = []
    for x in range (min,max + 1):
        if x % 2 == 0:
            evenNumbers.append(x)
            
          
    return evenNumbers

print(even_numbers(1,10))
