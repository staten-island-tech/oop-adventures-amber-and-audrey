user_input = (input("Enter a number: "))

def pal(user_input):
    if user_input == user_input[::-1]:
        print("palindrome")
    else:
        print("false")

pal(user_input)

# created new string or list if x = y