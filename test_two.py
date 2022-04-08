from unittest import TestCase
import unittest
from two import get_two


class Test(TestCase):
    def test_get_two(self):
        self.assertEqual(get_two(3), 8)


if __name__ == '__main__':
    unittest.main()



