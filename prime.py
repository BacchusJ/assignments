number = int(input("Enter your number to see if it is Prime or Not "))
def primey(number):
    if (number % 2) == 0:
        print(f"{number}This is an even number")
    else:
        print(f"{number}This is not an even number")
primey(number)
