def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: The result of the operation, or an error message for invalid operations or division by zero.
    """

    operation = operation.strip().lower() 

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"  
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
