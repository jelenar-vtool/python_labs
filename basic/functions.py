import random

# Global variable to store the previous random number
previous_random = None

def generate_random_number():
    """
    Generates a random number between 0 and 100.
    """
    return random.randint(0, 100)

def add_to_previous():
    """
    Adds the current random number to the previous one.
    If it's the first random number, returns the current random number.
    """
    global previous_random
    current_random = generate_random_number()
    if previous_random is None:
        previous_random = current_random
    else:
        previous_random += current_random
    return previous_random

# Example usage:
for _ in range(5):
    print("Current random number:", generate_random_number())
    print("Random number added to previous:", add_to_previous())
    print()