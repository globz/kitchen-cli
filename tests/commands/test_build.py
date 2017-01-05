
"""Tests for our `kitchen build` user action."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestBuild(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['kitchen', 'build'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hungry_for_pastries(self):
        output = popen(['kitchen', 'build'], stdout=PIPE).communicate()[0]
        self.assertTrue('You are hungry for pastries...' in output)
