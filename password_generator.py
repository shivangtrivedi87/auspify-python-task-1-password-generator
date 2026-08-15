import secrets
import string

        
def generate_password(length): 
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    password = [secrets.choice(letters),secrets.choice(digits),secrets.choice(punctuation) ]
    
    allcharacters = letters + digits + punctuation

    for _ in range(length -3):
        password.append(secrets.choice (allcharacters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def generate_multiple_passwords(length, count):
    passwords = []

    for _ in range(count):
        passwords.append(generate_password(length))

    return passwords

while True: 
    try:
        length = int(input ("Enter password length: ")) 
        if length < 3:
            print("Password length must be at least 3.")
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