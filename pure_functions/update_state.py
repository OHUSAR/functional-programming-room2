

from re import U


def update_state(current_state, message):
    updated_state = {
        **current_state,
    }
    for username in message:
        if username in updated_state:
            updated_state[username].append(message[username])
        else:
            updated_state[username] = [message[username]]
    return updated_state