def sum_of_even_numbers(numbers):
    even_sum = 0 # variable used to calculate sum of even numbers and store it

    
    for num in numbers:
        
        if num % 2 == 0:
            
            even_sum += num

    return even_sum # returns the result and result is stored in even_sum and the loop is continued until all even numbers are calculated

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, -8, -7,10,11,12,13,14,18]# list of numbers in the array
result = sum_of_even_numbers(numbers)# stores the result in a variable
print("Sum of even numbers:", result)# displays the sum as output
