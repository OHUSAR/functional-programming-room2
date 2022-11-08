
def post(input: str):
    input_parts = input.split()
    username = input_parts[0]
    message = ' '.join(input_parts[1:])
    return {username: message}
