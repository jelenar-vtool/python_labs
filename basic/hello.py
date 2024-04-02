# Global variable to store the previous number
previous_number = None

def get_five_numbers():
    """
    Gets five numbers from the user.
    Handles exceptions, specifically catches division by zero.
    """
    numbers = []
    for i in range(5):
        while True:
            try:
                number = float(input(f"Enter number {i+1}: "))
                if number == 0:
                    raise ValueError("Cannot divide by zero!")
                numbers.append(number)
                break
            except ValueError as ve:
                print("Error:", ve)
    return numbers

def divide_with_previous(numbers):
    """
    Divides each number by the previous number.
    """
    global previous_number
    results = []
    for number in numbers:
        if previous_number is None or previous_number == 0:
            results.append(number)
            previous_number = number
        else:
            try:
                result = number / previous_number
                results.append(result)
                previous_number = number
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
                results.append(number)
                previous_number = number
    return results

# Example usage:
numbers = get_five_numbers()
results = divide_with_previous(numbers)
print("Results of division with previous number:")
for i, result in enumerate(results):
    print(f"Number {i+1}: {result}")
