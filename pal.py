def Palabra():
    Palabra = input('Enter The Word: ')
    Palabra = Palabra.lower()
    RwordN = Palabra[::-1]
    if Palabra == RwordN:
        print("This Word is a Palindrome")
    else:
        print("This isn't a Palindrome")

Palabra()
