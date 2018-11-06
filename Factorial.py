def col(a):
    if a==1:

        n=int(input("Enter a Number: "))

        factorial = 1

        # check if the number is negative, positive or zero
        if n < 0:
           print("Sorry, factorial does not exist for negative numbers")
           return col(1)
        elif n == 0:
           print("The factorial of 0 is 1")
           return col(1)
        else:
           for i in range(1,n + 1):
               factorial = factorial*i
           print("The factorial of",n,"is",factorial)
           return col(1)

col(1)