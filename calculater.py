def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def divides(num1,num2):
    return num1 / num2

def avg(num1,num2):
    return (num1 + num2)/2

print("Please select a opration:\n  "\
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplicaton\n" \
      "4. Division\n" \
      "5. Average"  )

select = int(input("Select a operation from 1,2,3,4,5:  "))

number1 = int(input("Enter first number:  "))
number2 = int(input("Enter second number:  "))


if select == 1:
    print("sum of two number: = ",number1 ,"+", number2 ,"=", add(number1,number2))

elif select == 2:
    print("subtraction of two number: = ",number1 ,"-", number2, "=", sub(number1,number2))

elif select == 3:
    print("Multiplication of two number: = ",number1 ,"*", number2, "=", mul(number1,number2))

elif select == 4:
    print("divion of two number: = ",number1 ,"/", number2 ,"=", divides(number1,number2))

elif select == 5:
    print("sum of two number: = ","(",number1 ,"+", number2,")","/","2", "=" ,avg(number1,number2))

else :
    print("INVALID OPRATION PERFROM: SELECT AGAIN")