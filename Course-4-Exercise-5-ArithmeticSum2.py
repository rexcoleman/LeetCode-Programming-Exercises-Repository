
# A more readable version of the code that checks if the sum of the
# first n natural numbers equals n * (n + 1) // 2 for n from 1 to 100
# Define a function to check the formula for a single value of n

def check_sum_formula(n):
    # Calculate the sum of the first n natural numbers
    natural_sum = sum(range(1, n + 1))
    # Calculate the right-hand side of the formula
    formula_result = n * (n + 1) // 2
    # Return True if they are equal, False otherwise
    return natural_sum == formula_result


# Use a loop to check the formula for every n from 1 to 100
all_true = True
for n in range(1, 101):
    if not check_sum_formula(n):
        all_true = False
        break

# Print the result
print(all_true)