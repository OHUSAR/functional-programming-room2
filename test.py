import io
from unittest import TestCase, mock, skip
from main import main
from pure_functions.convert_input_to_arguments import convert_input_to_arguments
from pure_functions.post import post
from pure_functions.update_state import update_state
from pure_functions.convert_input_to_command import convert_input_to_command

class Test(TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        # Bob posted Message
        # Bob posted message2

        # ...

        # FACEBOOK WALL
        #     Bob posted 'message2' 1 minute ago
        #     Bob posted 'Message'  2 minute ago
        with mock.patch('builtins.input', side_effect=['Bob -> Message', 'Bob -> message2', 'Bob', 'exit']):
            main()


        self.assertEqual(mock_stdout.getvalue(), "Bob posted message2\nBob posted Message\n")

    """
    Commands always start with the user’s name.
        ● posting: <user name> -> <message>
        ● reading: <user name>
        ● following: <user name> follows <another user>
        ● wall: <user name> wall
    """

    def test_convert_input_to_command(self):
        self.assertEqual(convert_input_to_command('Bob -> Message'), 'post')
        self.assertEqual(convert_input_to_command('Bob'), 'read')
        self.assertEqual(convert_input_to_command('exit'), 'exit')
    
    def test_convert_input_to_arguments(self):
        self.assertEqual(convert_input_to_arguments('Bob -> Message', 'post'), ['Bob', 'Message'])
        self.assertEqual(convert_input_to_arguments('Bob', 'read'), ['Bob'])

    def test_post(self):
        self.assertEqual(post('Bob', 'My First Post'), {'Bob': 'My First Post'})

    def test_update(self):
        current_state = {}
        updated_state = update_state(current_state, {'Bob': 'Message'})
        self.assertEqual(updated_state, {'Bob': ['Message']})

    def test_update_if_same_user_posts_second_message(self):
        current_state = {'Bob': ['Message']}
        updated_state = update_state(current_state, {'Bob': 'Message2'})
        self.assertEqual(updated_state, {'Bob': ['Message', 'Message2']})