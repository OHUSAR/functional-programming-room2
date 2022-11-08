import io
from unittest import TestCase, mock
from main import main
from pure_functions.post import post
from pure_functions.update_state import update_state

class Test(TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=['Bob Message', 'Alice message', 'read', 'exit']):
            main()
        
        self.assertEqual(mock_stdout.getvalue(), "{'Bob': ['Message'], 'Alice': ['message']}\n")

    ###

    def test_post(self):
        self.assertEqual(post('Bob My First Post'), {'Bob': 'My First Post'})

    def test_update(self):
        current_state = {}
        updated_state = update_state(current_state, {'Bob': 'Message'})
        self.assertEqual(updated_state, {'Bob': ['Message']})

    def test_update_if_same_user_posts_second_message(self):
        current_state = {'Bob': ['Message']}
        updated_state = update_state(current_state, {'Bob': 'Message2'})
        self.assertEqual(updated_state, {'Bob': ['Message', 'Message2']})