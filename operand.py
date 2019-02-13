Number_One = int(input("Enter your number: " ))
Operation = input('''choose your equation
+ to add
- to subtract
* to multiply
/ to devide ''')
Number_Two = int(input("Enter your second number " ))


def operator (Number_One, Number_Two, operation):

    if operation == '+':
        Total = (Number_One + Number_Two)
        return(Total)

    elif operation == '-':
        Total = (Number_One - Number_Two)
        return(Total)

    elif operation == '*':
        Total = (Number_One * Number_Two)
        return(Total)

    elif operation == '/':
        Total = (Number_One / Number_Two)
        return(Total)

print(operator (Number_One, Number_Two, Operation))


