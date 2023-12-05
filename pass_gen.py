import random
import secrets
import string

def generate_password_part(min_length=5, max_length=10, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Determine password length within the specified range
    length = random.randint(min_length, max_length) 

    # Shuffle the characters using list conversion and shuffling
    password_part = ''.join(secrets.choice(all_chars) for _ in range(length))

    return password_part

def shuffle_password_parts(pass_parts):
    # Convert to list and shuffle for additional randomness
    password_list = list(''.join(pass_parts))
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    
    return password

# Example usage with a loop to generate multiple password parts
pass_parts_num = 3  # Change this number to generate a different count of password parts

pass_parts = [generate_password_part() for _ in range(pass_parts_num)]

# Shuffle the password parts and get the final password
password = shuffle_password_parts(pass_parts)

print("Generated Password Parts:", pass_parts)
print("Shuffled Password:", password)
print("Password Length:", len(password))
