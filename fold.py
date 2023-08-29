from functools import reduce

def join_strings(word_list):
    return reduce(lambda combined, word: combined + " " + word, word_list)

words = ["hello", "world"]
helloworld = join_strings(words)
print(helloworld)  
