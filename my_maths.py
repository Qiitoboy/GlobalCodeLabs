def calculate(operation ,num1, num2):
    if operation.lower() == "add":
        print (num1 + num2)
    elif operation.lower() == "subtract":
        print (num1 - num2)
    elif operation.lower() == "multiply":
        print (num1 * num2)
    elif operation.lower() == "divide":
        print (num1 / num2)

calculate("add",3,2)
calculate("ADD",3,8)
        
        

