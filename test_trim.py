#!/usr/bin/env python

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
        self.assertFalse(trim.is_text('/bin/bash'))
        self.assertFalse(trim.is_text('/usr/bin/env'))
        self.assertFalse(trim.is_text('non_existent_file'))

    def test_is_text_should_consider_symlinks_as_non_text(self):
        self.assertFalse(trim.is_text(os.path.join(ROOT_DIR, 'trim.py')))

    def test_is_text_should_consider_whitespace_only_as_text(self):
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
            temporary_file.write('     ')
            temporary_file.flush()

            self.assertTrue(trim.is_text(temporary_file.name))

    def test_is_text_should_consider_empty_files_as_non_text(self):
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
            temporary_file.write('')
            temporary_file.flush()

            self.assertFalse(trim.is_text(temporary_file.name))

    def test_system(self):
        text = 'abc   \n   1234  \n\n  \n'
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False,
                                         mode='w') as temporary_file:
            temporary_file.write(text)

        import subprocess
        process = subprocess.Popen([os.path.join(ROOT_DIR, 'trim'),
                                    temporary_file.name],
                                   stderr=subprocess.PIPE)
        process.communicate()
        self.assertEqual(0, process.returncode)

        with open(temporary_file.name) as input_file:
            self.assertEqual(trim.trim(text),
                             input_file.read())

        os.remove(temporary_file.name)


if __name__ == '__main__':
    unittest.main()
