import secrets
import string

        
characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length): 
    password = ""

    for _ in range(length):
        password += secrets.choice (characters)
    return password

def generate_multiple_passwords(length, count):
    passwords = []

    for _ in range(count):
        passwords.append(generate_password(length))

    return passwords

while True: 
    try:
        length = int(input ("Enter password length: ")) 

        if length <= 0:
            print ("Password length should be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter valid length.")

while True:
    try:
        count = int(input("How many passwords do you want to generate? "))

        if count <= 0:
            print("Number of passwords should be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

passwords = generate_multiple_passwords(length, count)

for index, password in enumerate(passwords, start=1):
    print(f"Password {index}: {password}")