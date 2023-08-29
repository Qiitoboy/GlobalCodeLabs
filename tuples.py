def partition(number):
    if number % 2 == 0:
        return (number, None)
    else:
        return (None, number)

def partition_list(numbers_list):
    odd_numbers = []
    even_numbers = []

    for num in numbers_list:
        even, odd = partition(num)
        if even is not None:
            even_numbers.append(even)
        if odd is not None:
            odd_numbers.append(odd)

    return (even_numbers, odd_numbers)


numbers = [1, 2, 3, 4, 5, 6]
result = partition_list(numbers)
print(result)  
