from apply_user_input import apply_user_input

def main():
    state = {}
    while True:
        user_input = input()
        if user_input == 'exit':
            break
        
        new_state, message_to_print = apply_user_input(user_input, state)

        state = new_state
        if message_to_print is not None:
            print(message_to_print)
        