import random
import string

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 1:
        return "Weak ❌"
    elif score == 2 or score == 3:
        return "Medium ⚠️"
    else:
        return "Strong 🔐"


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


print("🔐 Password Tool")
print("1. Check password strength")
print("2. Generate password")

choice = input("Choose option: ")

if choice == "1":
    pwd = input("Enter password: ")
    print("Strength:", check_strength(pwd))

elif choice == "2":
    print("Generated password:", generate_password())