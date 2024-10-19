# Function to find the oldest age
def find_oldest_age(ages):
    return max(ages)

# Input ages from the user in a single line
try:
    ages_input = input("Enter three ages separated by spaces: ")
    ages = list(map(int, ages_input.split()))

    if len(ages) != 3:
        raise ValueError("Please enter exactly three ages.")

    # Find and display the oldest age
    oldest_age = find_oldest_age(ages)
    print(f"The oldest age is: {oldest_age}")
except ValueError as e:
    print(f"Error: {e}. Please enter valid integers for ages.")
