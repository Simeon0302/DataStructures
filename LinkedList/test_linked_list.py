import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_add_first(self):
        ll = LinkedList()
        ll.add_first(1)
        self.assertEqual(str(ll), '[1]')
        ll.add_first(2)
        self.assertEqual(str(ll), '[2, 1]')

    def test_add_last(self):
        ll = LinkedList()
        ll.add_last(1)
        self.assertEqual(str(ll), '[1]')
        ll.add_last(2)
        self.assertEqual(str(ll), '[1, 2]')
        ll.add_last(3)
        self.assertEqual(str(ll), '[1, 2, 3]')

    def test_add_after(self):
        ll = LinkedList([1, 2, 3])
        ll.add_after(2, 4)
        self.assertEqual(str(ll), '[1, 2, 4, 3]')
        ll.add_after(3, 5)
        self.assertEqual(str(ll), '[1, 2, 4, 3, 5]')
        with self.assertRaises(Exception):
            ll.add_after(6, 7)

    def test_add_before(self):
        ll = LinkedList([1, 2, 3])
        ll.add_before(2, 4)
        self.assertEqual(str(ll), '[1, 4, 2, 3]')
        ll.add_before(1, 5)
        self.assertEqual(str(ll), '[5, 1, 4, 2, 3]')
        with self.assertRaises(Exception):
            ll.add_before(6, 7)

    def test_remove_node(self):
        ll = LinkedList([1, 2, 3, 4])
        ll.remove_node(3)
        self.assertEqual(str(ll), '[1, 2, 4]')
        ll.remove_node(1)
        self.assertEqual(str(ll), '[2, 4]')
        ll.remove_node(4)
        self.assertEqual(str(ll), '[2]')
        ll.remove_node(2)
        self.assertEqual(str(ll), '[]')
        with self.assertRaises(Exception):
            ll.remove_node(2)

    def test_get(self):
        ll = LinkedList([1, 2, 3])
        node = ll.get(1)
        self.assertEqual(node.data, 2)
        node = ll.get(0)
        self.assertEqual(node.data, 1)
        node = ll.get(2)
        self.assertEqual(node.data, 3)
        with self.assertRaises(Exception):
            ll.get(3)

    def test_reverse(self):
        ll = LinkedList([1, 2, 3])
        ll.reverse()
        self.assertEqual(str(ll), '[3, 2, 1]')
        ll = LinkedList([1])
        ll.reverse()
        self.assertEqual(str(ll), '[1]')
        ll = LinkedList()
        ll.reverse()
        self.assertEqual(str(ll), '[]')

    def test_clear(self):
        ll = LinkedList([1, 2, 3])
        ll.clear()
        self.assertEqual(str(ll), '[]')
        ll.clear()
        self.assertEqual(str(ll), '[]')

if __name__ == '__main__':
    unittest.main()