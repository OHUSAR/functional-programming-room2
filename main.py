from pure_functions.post import post


def get_input(text = ''):
    return input(text)

def main():
    state = {}
    ans = get_input()
    
    result = post(ans)
    update(result)
