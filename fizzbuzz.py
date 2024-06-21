def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:#  and operator checks if the reminder of both the conditions is true
            print("FizzBuzz")
        elif i % 3 == 0:# if the above condition fails to satisfy the need elif conditional statement is used 
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
