from unittest import TestCase
from pure_functions.post import post

class Test(TestCase):
    def test_post(self):
        self.assertEqual(post('Bob My First Post'), {'Bob': 'My First Post'})