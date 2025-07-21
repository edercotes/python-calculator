def validate_input(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_output(result):
    return f"The result is: {result}"