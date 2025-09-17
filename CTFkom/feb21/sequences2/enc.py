secret_word = ''


def secret_number_sequence(start_pos: int, length: int) -> list[int]:
    # Oh no the sequence code is gone, but I remember it is almost the same as in the first challenge!
    ...

sequence = secret_number_sequence(start_pos=<DELETED>, length=len(secret_word))

encrypted_secret = [ord(char) * sequence[i] for i, char in enumerate(secret_word)]

for num in encrypted_secret:
    print(num)
