from unittest import TestCase
from pure_functions.post import post
from pure_functions.update_state import update_state

class Test(TestCase):
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