from unittest import TestCase
import unittest
from test import get_vowel_num


class Test(TestCase):
    def test_get_vowel_num(self):
        self.assertEqual(get_vowel_num("apple"), 2)


if __name__ == '__main__':
    unittest.main()
