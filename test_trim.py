"""Test suite for trim."""

import unittest

import trim


class TrimTests(unittest.TestCase):

    def test_trim(self):
        self.assertEqual(
            """
abc
   123
test
""".lstrip(),
            trim.trim("""

abc\t
   123\t      \t\t
test



"""))

    def test_trim_with_empty_string(self):
        self.assertEqual('\n', trim.trim(''))
        self.assertEqual('\n', trim.trim('\n'))


if __name__ == '__main__':
    unittest.main()
