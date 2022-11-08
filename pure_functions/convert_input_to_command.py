
"""
Commands always start with the user’s name.
    ● posting: <user name> -> <message>
    ● reading: <user name>
    ● following: <user name> follows <another user>
    ● wall: <user name> wall
"""

def convert_input_to_command(input: str):
    if '->' in input:
        return 'post'
    elif input == 'exit':
        return 'exit'
    else:
        return 'read'