#create user defined function
def check_palindrome(number):
    original_number = number
    reversed_number = 0
    
#use while loop to reverse given number

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

#if else statement to check reverse and original number is the same
    
    if original_number == reversed_number:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")

#ask user for input

user_input = int(input("Enter a number: "))
check_palindrome(user_input)
