# Calculator

def get_number(prompt):
    """Prompts user for number, handles invalid input with loop."""
    while True:
        try:
            user_input = input(prompt).strip()
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Gets valid operation from user with validation."""
    valid_ops = {'+', '-', '*', '/'}
    while True:
        op = input('Enter operation (+, -, *, /): ').strip()
        if op in valid_ops:
            return op
        print("Invalid operation. Use only +, -, *, or /.")
        
def calculate(num1, num2, operation):
    """Performs calculation, handles division by zero."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return None
        return num1 / num2

    # Invalid ops caught by get_operation(), this shouldn't trigger
    return None


def main():
    """Main calculator loop."""
    print("=== Simple Command-Line Calculator ===\n")
    while True:
        # Get inputs
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        op = get_operation()
        # Calculate and display
        result = calculate(num1, num2, op)
        if result is not None:
            # Smart formatting avoids float precision issues (0.1+0.2=0.3)
            print(f"Result: {num1} {op} {num2} = {result:.10g}\n")
        # Errors already printed by calculate()
        # Continue?
        again = input("Another calculation? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            break
    print("Thanks for using the calculator. Goodbye!")
    
main()