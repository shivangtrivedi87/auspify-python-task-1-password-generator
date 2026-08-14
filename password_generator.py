import secrets
import string

        
characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length): 
    password = ""

    for _ in range(length):
        password += secrets.choice (characters)
    return password


while True: 
    try:
        length = int(input ("Enter password length: ")) 

        if length <= 0:
            print ("Password length should be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter valid length.")

password = generate_password(length)
print("Generated Password: "+password)