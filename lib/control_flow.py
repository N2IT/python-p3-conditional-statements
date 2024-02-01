
#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    # username needs to equal admin OR admin
    # password needs to equal 12345
    # all conditions need to be met to return "Access granted" else return "Access denied"
    username = username.lower()
    # if username == "admin" and password == "12345":
    #     return "Access granted"
    # else:
    #     return "Access denied"

    return "Access granted" if username == "admin" and password == "12345" else "Access denied"

def hows_the_weather(temperature):
    # your code here
    # temp above 85, return "too hot!"
    # temp between 40 and 65 return "little chilly"
    # temp below 40 return "its brisk"
    # else "its perfect"
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    # if multiple of 3 return 'Fizz'
    # if multiple of 5 return 'Buzz'
    # if multiples of 3 and 5 return 'FizzBuzz'
    # else return num
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num

def calculator(operation, num1, num2):
    # your code here
    pass
