def reverse_string(input_string): #TAKES THE INPUT STRING AS THE PARAMETER
    reversed_str = "" # STORES THE FINAL STRING
    for char in input_string[::-1]: #[::-1] ITS A SLICING PROCESS USED IN PYTHON TO REVERSE A STRING AND THE LOOP IS CONTINUED UNTIL ALL THE CHARECTERS IN THE STRING ARE SLICED AND REVERSED A
        reversed_str += char # EVERY CHARECTER IS SLICED AND REVERSE OF IT IS STORED 
    return reversed_str # RTURNS THE VALUE OF REVERSED STRING INTO THE input_string

# Example usage:
input_string = "GTARUN"
result = reverse_string(input_string)
print("Reversed string:", result)
