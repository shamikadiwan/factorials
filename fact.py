def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= 1
  return result
    number = int(input("Enter number for finding its factorial "))

    if number < 0:
    print("Factorial of number can't find for its negative number")

                 else:
                   print(f"Factorial of {number} is : {factorial_Iterative:(number)}")


