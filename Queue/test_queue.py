import unittest
from my_queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue('a')
        self.assertEqual(str(q), "['a']")
        q.enqueue('b')
        self.assertEqual(str(q), "['b', 'a']")
        q.enqueue('c')
        self.assertEqual(str(q), "['c', 'b', 'a']")

    def test_dequeue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(str(q), "['c', 'b']")
        self.assertEqual(q.dequeue(), 'b')
        self.assertEqual(str(q), "['c']")
        self.assertEqual(q.dequeue(), 'c')
        self.assertEqual(str(q), '[]')
        with self.assertRaises(Exception):
            q.dequeue()

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue('a')
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_peek(self):
        q = Queue()
        q.enqueue('a')
        self.assertEqual(q.peek(), 'a')
        q.enqueue('b')
        self.assertEqual(q.peek(), 'a')
        q.dequeue()
        self.assertEqual(q.peek(), 'b')
        q.dequeue()
        with self.assertRaises(Exception):
            q.peek()

    def test_clear(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        q.clear()
        self.assertTrue(q.is_empty())
        with self.assertRaises(Exception):
            q.peek()
        with self.assertRaises(Exception):
            q.dequeue()

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.size(), 2)
        q.enqueue('c')
        self.assertEqual(q.size(), 3)
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertEqual(q.size(), 0)
        with self.assertRaises(Exception):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()