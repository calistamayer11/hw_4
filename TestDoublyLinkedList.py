from DoublyLinkedList import DoublyLinkedList as DLL, Node
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        """adds items to front, then removes from front"""
        dll = DLL()
        n = 100

        for j in range(
            5
        ):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_first(), n - 1 - i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        """adds items to end, then removes from end"""
        dll = DLL()
        n = 100

        for j in range(
            5
        ):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_last(), n - 1 - i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        """various add/remove patterns"""
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(
            5
        ):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(
            5
        ):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(
            5
        ):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i % 2:
                    dll.add_last(i)  # odd numbers - add last
                else:
                    dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                if i % 2:
                    self.assertEqual(
                        dll.remove_last(), n - i
                    )  # odd numbers: remove last
                else:
                    self.assertEqual(
                        dll.remove_first(), n - 2 - i
                    )  # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        """Tests if list has the correct nodes with the given range"""
        dll = DLL(range(4))
        self.assertTrue(3 in dll)
        self.assertFalse(7 in dll)

    def test_neighbors(self):
        """Test neighbors method, returns a tuple of the neighbors items"""
        dll = DLL(range(7))
        number = dll.neighbors(4)
        test_pair = (3, 5)
        # test if the neighbors of node 4 are 3 and 5
        self.assertEqual(number, test_pair)

        number_head = dll.neighbors(0)
        test_pair_head = (None, 1)
        # test if the neighbors of the head are None and 1
        self.assertEqual(number_head, test_pair_head)

        number_tail = dll.neighbors(6)
        test_pair_tail = (5, None)
        # test if the neighbors of the tail are 5 and None
        self.assertEqual(number_tail, test_pair_tail)

    def test_remove_item(self):
        """Test removing a node from a dll, returns removed node"""
        dll = DLL(range(5))
        # dll should have 5 nodes
        self.assertEqual(len(dll), 5)
        remove = dll.remove_node(2)
        # Now dll shoud have 4 nodes after removing item 2
        self.assertEqual(len(dll), 4)
        self.assertIsInstance(remove, Node)
        self.assertEqual(remove.item, 2)

        # already removed 2, cannot remove again
        with self.assertRaises(RuntimeError):
            dll.remove_node(2)


unittest.main()
