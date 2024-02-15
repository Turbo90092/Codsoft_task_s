import random
import string


password = input('generate password with minimum of 8 to 11 characters: ')

def generate_password():
    while True:
        length = random.randint(8, 11)
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))

        for i in range(length - 3):
            password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

        random.shuffle(password)
        generated_password = ''.join(password)

        if 8 <= len(generated_password) <= 11:
            return generated_password

generated_password = generate_password()
print("Generated Password:", generated_password)




