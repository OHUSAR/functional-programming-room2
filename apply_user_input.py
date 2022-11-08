from pure_functions.post import post
from pure_functions.update_state import update_state
from pure_functions.convert_input_to_command import convert_input_to_command
from pure_functions.convert_input_to_arguments import convert_input_to_arguments

def apply_user_input(user_input, state):
    command = convert_input_to_command(user_input)
    args = convert_input_to_arguments(user_input, command)
    if command == 'read':
        messages_to_print = []
        for message in state[args[0]][::-1]:
            messages_to_print.append(f"{args[0]} posted {message}")
        return state, '\n'.join(messages_to_print)
    else:
        new_state = update_state(state, post(*args))
        return new_state, None
