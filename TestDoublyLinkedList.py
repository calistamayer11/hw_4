from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        "adds items to front, then removes from front"
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
        "adds items to end, then removes from end"
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
        "various add/remove patterns"
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
        dll = DLL(range(4))
        self.assertTrue(3 in dll)
        self.assertFalse(7 in dll)

    def test_neighbors(self):
        dll = DLL(range(7))
        number = dll.neighbors(4)
        test_pair = (3, 5)
        self.assertEqual(number, test_pair)

        number_head = dll.neighbors(0)
        test_pair_head = (None, 1)
        self.assertEqual(number_head, test_pair_head)

        number_tail = dll.neighbors(6)
        test_pair_tail = (5, None)
        self.assertEqual(number_tail, test_pair_tail)

    def test_remove_item(self):
        dll = DLL(range(5))
        remove = dll.remove_node(0)
        test_pair = (None, 1)
        self.assertEqual(remove, test_pair)


unittest.main()
