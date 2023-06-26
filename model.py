from constraint import Problem

def solve_cryptography_problem(plaintext_alphabet, ciphertext_alphabet):
    problem = Problem()

    # Define the variables and domains
    problem.addVariables(plaintext_alphabet, ciphertext_alphabet)

    # Define the constraint: all variables must have unique assignments
    problem.addConstraint(lambda *letters: len(set(letters)) == len(letters), plaintext_alphabet)

    # Solve the problem
    solutions = problem.getSolutions()

    # Print the solutions
    for solution in solutions:
        print("Mapping:")
        for plaintext_letter, ciphertext_letter in solution.items():
            print(plaintext_letter, "->", ciphertext_letter)
        print("")

    # Print the plaintext and ciphertext alphabets
    print("Plaintext Alphabet:", plaintext_alphabet)
    print("Ciphertext Alphabet:", ciphertext_alphabet)

# Example usage
plaintext_alphabet = ['A', 'B', 'C', 'D']
ciphertext_alphabet = ['X', 'Y', 'Z', 'W']
solve_cryptography_problem(plaintext_alphabet, ciphertext_alphabet)
