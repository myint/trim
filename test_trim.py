"""Test suite for trim."""

import os
import sys
import unittest

import trim


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


class TrimTests(unittest.TestCase):

    def test_trim(self):
        self.assertEqual(
            """
abc
   123
test
""",
            trim.trim("""
abc\t
   123\t      \t\t
test



"""))

    def test_trim_with_empty_string(self):
        self.assertEqual('\n', trim.trim(''))
        self.assertEqual('\n', trim.trim('\n'))

    def test_trim_should_leave_leading_whitespace(self):
        self.assertEqual(' abc\n', trim.trim(' abc\n'))

    def test_is_text(self):
        self.assertTrue(trim.is_text(os.path.join(ROOT_DIR, 'README.rst')))
        self.assertTrue(trim.is_text(os.path.join(ROOT_DIR, 'trim')))
        self.assertFalse(trim.is_text(sys.executable))

    def test_is_text_should_consider_symlinks_as_non_text(self):
        self.assertFalse(trim.is_text(os.path.join(ROOT_DIR, 'trim.py')))


if __name__ == '__main__':
    unittest.main()
