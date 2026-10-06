import random
import string

# Ask the user for password length
length = int(input("Enter the password length: "))

# Combine letters, numbers, and special characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)