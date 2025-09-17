secret_word = ''


def secret_number_sequence(length: int) -> list[int]:
    # Oh no the sequence code is gone
    ...


# Generate a secret sequence with the same length as the secret
sequence = secret_number_sequence(length=len(secret_word))

# Initialize an empty list to store the encrypted values
encrypted_secret = []

# Iterate over each character in the secret along with its corresponding number
for character, secret_number in zip(secret_word, sequence):
    # Convert the character to its Unicode code point
    unicode_value = ord(character)

    # Multiply the Unicode value by the secret number to encrypt
    encrypted_value = unicode_value * secret_number

    # Append the encrypted value to the list
    encrypted_secret.append(encrypted_value)

# Output the encrypted values
for num in encrypted_secret:
    print(num)
