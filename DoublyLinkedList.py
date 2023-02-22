# Do not modify this class
class Node:
    "Node object to be used in DoublyLinkedList"

    def __init__(self, item, _next=None, _prev=None):
        "initializes new node objects"
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        "String representation of Node"
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        "Construct a new DLL object"
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()  # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        "returns number of nodes in DLL"
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        """adds item to front of dll"""
        if item in self._nodes:
            raise RuntimeError("Item already in dll")

        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1

        # if that was the first node
        if len(self) == 1:
            self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else:
            self._head._next._prev = self._head
        self._nodes[item] = self._head

    def add_last(self, item):
        """adds item to end of dll"""
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1

        # if that was the first node
        if len(self) == 1:
            self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else:
            self._tail._prev._next = self._tail

        self._nodes[item] = self._tail

    def remove_first(self):
        """removes and returns first item"""
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0:
            self._tail = None

        else:
            self._head._prev = None

        del self._nodes[item]

        return item

    def remove_last(self):
        """removes and returns last item"""
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0:
            self._head = None

        else:
            self._tail._next = None
        del self._nodes[item]

        return item

    # TODO: Add a docstring and implement
    def __contains__(self, item):
        return item in self._nodes

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        """returns the previous and next node in the dictionary"""
        if item not in self._nodes:
            raise RuntimeError("Item not found, cannot remove")

        node = self._nodes[item]

        if node._prev is not None:
            previous_node = node._prev.item
        else:
            previous_node = None

        if node._next is not None:
            next_node = node._next.item
        else:
            next_node = None
        next_node = node._next.item if node._next is not None else None
        return previous_node, next_node

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        """removes the node in the list"""
        if not item in self._nodes:
            raise RuntimeError("Item not found, cannot remove")

        node = self._nodes[item]
        if node == self._head and node == self._tail:
            self._head = None
            self._tail = None
        elif node == self._head:
            self.remove_first()
        elif node == self._tail:
            self.remove_last()
        else:
            node._prev._next = node._next
            node._next._prev = node._prev
            del self._nodes[item]
            self._len -= 1

        return node


if __name__ == "__main__":
    dll = DoublyLinkedList(range(5))
    dll.add_first(3)
    print(dll)
    dll.add_first(3)
    print(dll)
