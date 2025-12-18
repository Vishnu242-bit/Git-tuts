Code.py
Code.py ("saving code"):def save_code_to_file(code_string, filename):
    """Saves the given code string to a file with the specified filename."""
    with open(filename, 'w') as file:
        file.write(code_string)