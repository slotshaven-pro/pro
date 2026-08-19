def addNum(num1, num2):
    total = num1 + num2
    return total


value1 = 0
value2 = 0
value1 = int(input("Enter the first number: "))  # Input first number
value2 = int(input("Enter the second number: "))  # Input second number

# Invoking the function addNum() and Printing the Output
print(f"The sum of {value1} and {value2} is {addNum(value1, value2)}")
