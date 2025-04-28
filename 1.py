from math import factorial as math_factorial

powered_numbers = [number**2 for number in range(1, 11)]
print(f"1. {powered_numbers}")

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_mapping = {weekday: index + 1 for index, weekday in enumerate(weekdays)}
print(f"2. {weekday_mapping}")

frameworks = ["Flask", "Starlette", "SciPy", "PYTORCH", "Polars", "STARLETTE", "python", "secrets"]
unique_frameworks = {fw.lower() for fw in frameworks}
print(f"3. {unique_frameworks}")

values = [2, 5, 7, 34, 61, 12, 9, 6]
odd_numbers = [value for value in values if value % 2 != 0]
print(f"4. {odd_numbers}")

custom_factorial_mapping = {i: math_factorial(i) for i in range(1, 6)}
print(f"5. {custom_factorial_mapping}")

def calculate_my_factorial(input_number):
    if input_number == 0:
        return 1
    else:
        product = 1
        for i in range(1, input_number + 1):
            product *= i
        return product

custom_factorial_numbers = {i: calculate_my_factorial(i) for i in range(1, 6)}
print(f"5 (custom factorial). {custom_factorial_numbers}")
