import random
import secrets
import string
import bcrypt

def generate_password_part(random_length=random.randint(10,21), include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Determine password length within the specified range
    length = random_length 

    # Shuffle the characters using list conversion and shuffling
    password_part = ''.join(secrets.choice(all_chars) for _ in range(length))
    
    return password_part

def shuffle_password_parts(pass_parts):
    # Convert to list and shuffle for additional randomness
    password_list = list(''.join(pass_parts))
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    
    return password

#Make shit more convoluted!
def hashing(temp):
    byte1 = temp.encode('utf-16-be')
    byte2 = temp.encode('utf-16-le')
    byte3 = temp.encode('utf-8')
    bytes = byte1 + byte2 + byte3
    salts = bcrypt.gensalt(random.randint(5,11))
    hash = bcrypt.hashpw(bytes, salts)
    return hash

# Example usage with a loop to generate multiple password parts
pass_parts_num = random.randint(2,4)  # Change this number to generate a different count of password parts

pass_parts = [generate_password_part() for _ in range(pass_parts_num)]


# Shuffle the password parts and get the temp
final_password = shuffle_password_parts(pass_parts)

#Masking
hashed = hashing(final_password)
final_pass_masked = hashed[0:len(hashed):5].hex()

print("Password: " ,final_password)
print("Mask: " ,final_pass_masked)
