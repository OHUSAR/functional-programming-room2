from pure_functions.post import post
from pure_functions.update_state import update_state
from pure_functions.convert_input_to_command import convert_input_to_command
from pure_functions.convert_input_to_arguments import convert_input_to_arguments


def main():
    state = {}
    while True:
        user_input = input()
        command = convert_input_to_command(user_input)
        args = convert_input_to_arguments(user_input, command)
        if command == 'read':
            for message in state[args[0]][::-1]:
                print(f"{args[0]} posted {message}")
        elif command == 'exit':
            break
        else:
            state = update_state(state, post(*args))
        