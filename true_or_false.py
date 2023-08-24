
def true_or_false(string_input,letter):
    for char in string_input:
        if char == letter:
            return "true"
        else:
            return "false"

string_input = input("enter a string")
letter = input("enter a letter to search from the string")

print(true_or_false(string_input,letter))