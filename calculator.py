# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def calculate(expression):
    try:
        # Evaluate the expression using eval()
        result = eval(expression)
        return result
    except (SyntaxError, ZeroDivisionError) as e:
        return str(e)

if __name__ == "__main__":
    print("Welcome")
    print("Enter an arithmetic expression or 'exit' to quit.")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        try:
            result = calculate(user_input)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
