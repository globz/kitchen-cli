"""Tests for our `kitchen add` user action."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestAdd(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['kitchen', 'add'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_gathering_delicious_pastries(self):
        output = popen(['kitchen', 'add'], stdout=PIPE).communicate()[0]
        self.assertTrue('You are now gathering ingredients for your delicious pastries...' in output)
