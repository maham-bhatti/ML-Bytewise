import re

name = input('Enter your name: ')
age = input('Enter your age: ')
email = input('Enter your email: ')
num = input('Enter your favorite number: ')

dict = {
    "name": name,
    "age": age,
    "email": email,
    "favorite_number": num
}

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

if not valid_email(email):
    print("Invalid email format. Please enter a valid email.")
else:
    print("Hello", name, "you are", age, "years old, your email is", email, "and your favorite number is",num )




