import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push('a')
        self.assertEqual(str(s), "['a']")
        s.push('b')
        self.assertEqual(str(s), "['a', 'b']")
        s.push('c')
        self.assertEqual(str(s), "['a', 'b', 'c']")

    def test_pop(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.pop(), 'c')
        self.assertEqual(str(s), "['a', 'b']")
        self.assertEqual(s.pop(), 'b')
        self.assertEqual(str(s), "['a']")
        self.assertEqual(s.pop(), 'a')
        self.assertEqual(str(s), '[]')
        with self.assertRaises(Exception):
            s.pop()

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push('a')
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())

    def test_peek(self):
        s = Stack()
        s.push('a')
        self.assertEqual(s.peek(), 'a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
        s.pop()
        self.assertEqual(s.peek(), 'a')
        s.pop()
        with self.assertRaises(Exception):
            s.peek()

    def test_clear(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        s.clear()
        self.assertTrue(s.is_empty())
        with self.assertRaises(Exception):
            s.peek()
        with self.assertRaises(Exception):
            s.pop()

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push('a')
        s.push('b')
        self.assertEqual(s.size(), 2)
        s.push('c')
        self.assertEqual(s.size(), 3)
        s.pop()
        self.assertEqual(s.size(), 2)
        s.pop()
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)
        with self.assertRaises(Exception):
            s.pop()


if __name__ == '__main__':
    unittest.main()
