import string
from itertools import permutations

# Substitution cipher encryption function
def encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    ciphertext = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
    for char in plaintext:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if char.isupper():
                ciphertext += key[index].upper()
            else:
                ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

# Constraint Satisfaction Problem solver function
def solve_csp(ciphertext, alphabet, permutations):
    for perm in permutations:
        key = {alphabet[i]: perm[i] for i in range(len(alphabet))}
        plaintext = encrypt(ciphertext, key)
        # Check if the decrypted plaintext makes sense
        if "the" in plaintext.lower() and "python" in plaintext.lower():
            return plaintext
    return None

# Example usage
ciphertext = "L pmtz tnt tbiitadtz btwditg."
alphabet = string.ascii_lowercase
perms = permutations(alphabet)
plaintext = solve_csp(ciphertext, alphabet, perms)

print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)
