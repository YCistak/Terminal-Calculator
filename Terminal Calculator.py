def calculator():
    print("Python Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit.\n")
    

    while True:
        operation = input("Choose an operation (+, -, *, /) or : ").strip()
        if operation.lower() == "q":
            break
        

        if operation not in {"+", "-", "*", "/"}:
            print("Invalid operation.\n")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if operation == "+":
                result = x + y
            elif operation == "-":
                result = x - y
            elif operation == "*":
                result = x * y
            elif operation == "/":
                if y == 0:
                    print("Error: Division by zero.\n")
                    continue
                result = x / y

            print(f"Result: {result}\n")

        except ValueError:
            print("Please enter valid numbers.\n")


if __name__ == "__main__":
    calculator()

