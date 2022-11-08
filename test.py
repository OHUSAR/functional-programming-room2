from unittest.mock import patch
from unittest import TestCase

from main import answer

class Test(TestCase):
    @patch('main.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('main.get_input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')