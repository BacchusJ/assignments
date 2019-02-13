def factorial():
    num = int(input("Enter Your Number Here" ))
    fact=1
    while num > 0:
        fact=fact*num
        num=num-1
    print("Factorial Number is: ")
    print(fact)

factorial()
