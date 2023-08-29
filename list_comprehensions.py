numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive = list(filter(lambda x: x>0, numbers))
print(positive)


#a list containing only the even numbers from a list:

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# a list containing tuples of the uppercase version and the length of alist of words

words = ["hello", "my", "name", "is", "Sam"]
uppercase_len = [(lambda word: (word.upper(), len(word)))(word) for word in words]
print(uppercase_len)
            
