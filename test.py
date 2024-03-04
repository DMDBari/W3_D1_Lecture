from unittest import TestCase

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_general1(self):
        self.assertEqual(solution('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
    def test_no_spaces(self):
         self.assertEqual(solution('apple'), 'elppa')
    def test_not_reversing(self):
        self.assertEqual(solution('a b c d'), 'a b c d')
    def test_double_spaces(self):
        self.assertEqual(solution('double  spaced  words'), 'elbuod  decaps  sdrow')