number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
proc = input("Enter the process (*,/,+,-):")
if (proc=='*'):
   print(number1*number2)
elif(proc=='/'):
    print(number1/number2)
elif(proc=='+'):
    print(number1+number2)
else:
    print(number1-number2)

