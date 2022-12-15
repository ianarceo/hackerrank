import random

# Function to generate a password
def generate_password(length):
  password = ""
  # List of characters to choose from
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};:'\"<>,.?/"
  
  # Generate a password of the specified length
  for i in range(length):
    password += random.choice(chars)
    
  # Return the generated password
  return password

# Test the password generator
print(generate_password(8))  # Output: eg. "w4V6Bh8#"
print(generate_password(12)) # Output: eg. "a3!fB5gL7@m9D"
print(generate_password(16)) # Output: eg. "g5J7Fp3#h4V1@m6D8"
