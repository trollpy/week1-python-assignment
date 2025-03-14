def calcualtor():
    """
    A simple calculator program with basic operations.
    """ 
    print ("Welcome to the calculator program")
    
    num1 = float(input("Please enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Please enter the second number: "))
    result = 0
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        return result
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        return result
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        return result
    elif operator == '/':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
        return result
    else:
        print("Invalid operator")
        return None
    calculator()
    return result

calcualtor()