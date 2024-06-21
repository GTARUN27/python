def find_maximum_number(numbers):
    

    # Initialize the maximum number to the first element in the list
    max_number = numbers[0]

    
    for num in numbers:
        # Update the maximum number if the current number is greater
        if num > max_number:
            max_number = num

    return max_number

# Example usage:
numbers = [3, 1, -5, 7, -2, 8, -10,100,24,33 44]
result = find_maximum_number(numbers)
print("Maximum number:", result)
