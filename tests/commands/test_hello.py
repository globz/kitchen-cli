
"""Tests for our `kitchen hello` user action."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['kitchen', 'hello'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['kitchen', 'hello'], stdout=PIPE).communicate()[0]
        self.assertTrue('Hello, world!' in output)
