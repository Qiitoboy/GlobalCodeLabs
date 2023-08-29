numbers = [2,4,12, 1,13,5,17,23,45,82]
is_even = list(filter((lambda x : x %2 == 0),numbers))
print(is_even)

# odd numbers

is_odd = list(filter((lambda x : x % 2 != 0 ) , numbers))
print(is_odd)