
num1=float(input("Enter a number:"))
operand = input("Enter the operand: (+, -, *, /): ")
num2=float(input("Enter the second number:"))

if operand == "+":
    result = num1 + num2
    print(num1,operand,num2, "=",result)
elif operand == "-":
    result = num1 - num2
    print(num1,operand,num2, "=",result)
elif operand=="*":
    result =num1 * num2
    print("The answer is:",result)
elif operand=="/":
    if num2 != 0:
        result = num1 / num2
        print(num1,operand,num2, "=",result)
    else:
        print("Error: Cannot divide by zero.")
else :
    print("Please enter a valid operand")        
