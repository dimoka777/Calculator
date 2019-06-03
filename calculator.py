firstNumber = eval(input("Please input first number: "))
secondNumber = eval(input("Please input second number: "))
operator = input("Operator: ")
if operator == '+':
    result = firstNumber + secondNumber
if operator == '-':
    result = firstNumber - secondNumber
if operator == '/':
    if secondNumber == 0:
        result = "You can not devide to Zero!"
    else:
        result = firstNumber / secondNumber
if operator == '*' :
    result = firstNumber * secondNumber
print(result)

