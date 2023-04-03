# Factorial Algorythm

def Factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1

    return result

print(Factorial(5))
print(Factorial(6))
print(Factorial(10))