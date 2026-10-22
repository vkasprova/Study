# Drafts for lecture-01
foo = "Hello, World!"
print(foo)

print()
print(3 - 1000) # This will print a negative number
print(1000 - 3) # This will print a positive number

print()
def sum_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

result = sum_numbers(5, 3)
print(result)


print()
mod = abs(-5)
print("module:",mod)

print()
print("===Simple CLI calculator===")
a = b = 2
print("a: ", a)
print("b: ", b)
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)

print()

a = int(input("Enter 'a' number: "))
b = int(input("Enter 'b' number: "))
print("a + b = ", a + b)
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    print(f"Result: {a + b}")
elif operation == "-":
    print(f"Result: {a - b}")
elif operation == "*":
    print(f"Result: {a * b}")
elif operation == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
#elif operation != "+" or "-" or "*" or "/" :
else:
    print("Invalid operation. Please enter one of proposed operations.")

