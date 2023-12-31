nt(input("Enter the first number: "))
   num2 = int(input("Enter the second number: "))
   sum = num1 + num2
   div = num1 / num2
   mul = num1 * num2
   sub = num1 - num2

   print("Sum:", sum)
   print("Mul:", mul)
   print("Div:", div)
   print("Sub:", sub)

except ZeroDivisionError as e:
    print("Error!", e)
    print("Division by Zero is not accepted")
