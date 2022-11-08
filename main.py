from pure_functions.post import post
from pure_functions.update_state import update_state


def get_input(text = ''):
    return input(text)

def main():
    state = {}
    while True:
        command = get_input()

        if command == 'read':
            print(state)
        elif command == 'exit':
            break
        else:
            state = update_state(state, post(command))
        