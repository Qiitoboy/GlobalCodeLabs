
def evens(my_list):
     sum_result = 0
     for  x in my_list:
        if x % 2 == 0:
            sum_result = sum_result + x
            
     print(sum_result)

evens([2,3,4,5,6,7,8,])



#asking for a users age and telling them whether they are old or not
def get_age():
    age = int(input("what is your age"))
    if age > 18:
        print("you are old")
    else:
        print("you are not that old, you are a kid")    
    return ("And your age is " + " " +str(age))



print(get_age())


