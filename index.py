
num1=float(input("Enter a number:"))
operand = input("Enter the operand: (+, -, *, /): ")
num2=float(input("Enter the second number:"))

if operand == "+":
    result = num1 + num2
    print("The answer is:", result)
elif operand == "-":
    result = num1 - num2
    print("The answer is:", result)
elif operand=="*":
    result =num1 * num2
    print("The answer is:",result)
elif operand=="/":
    result =num1/num2
    print("The answer is:",result)
else :
    print("Please enter a valid operand")        
