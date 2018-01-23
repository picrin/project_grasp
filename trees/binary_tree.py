class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return "[{}, {}, {}]".format(self.left, self.value, self.right)
    def equal(self, n):
        if n is None:
            return False
        if self.value != n.value:
            return False
        if self.left is None:
            left_equal = n.left is None
        else:
            left_equal = self.left.equal(n.left)
        if self.right is None:
            right_equal = n.right is None
        else:
            right_equal = self.right.equal(n.right)
        return left_equal and right_equal
    def perm_equal(self, n):
        # Two binary trees A and B are perm-equal if there exists a way to swap left and right children in A
        # so that one gets a tree which is equal to B.
        pass

# Test cases

assert Node(4).equal(Node(4)) is True
a = Node(4)
a.left = Node(5)
b = Node(4)
b.left = Node(5)
assert a.equal(b) is True
assert Node(4).equal(None) is False
b.left = Node(6)
assert a.equal(b) is False
b.left = Node(5)
c = Node(4)
d = Node(4)
c.right = Node(5)
d.right = Node(5)
assert c.equal(d) is True
a.right = Node(6)
b.right = Node(6)
assert a.equal(b) is True
a.right = Node(3)
assert a.equal(b) is False
e = Node(4)
d = Node(4)
assert e.perm_equal(d) is True
e.left = Node(5)
e.left.left = Node(5)
e.left.right = Node(5)
e.right = Node(5)
e.right.left = Node(5)
e.right.right = Node(5)
d.left = Node(5)
d.left.left = Node(5)
d.left.right = Node(5)
d.right = Node(5)
d.right.left = Node(5)
d.right.right = Node(5)
assert e.perm_equal(d) is True
d.right.right.right = Node(5)
assert e.perm_equal(d) is False
d.right.right.right = None
assert e.perm_equal(d) is True
d.right.value = 3
assert e.perm_equal(d) is False
