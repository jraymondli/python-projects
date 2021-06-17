import os


class TreeNode:

    def is_leaf(self) -> bool:
        return self._isLeaf


class LeafNode(TreeNode):
    def __init__(self):
        self._isLeaf = True


class GreaterThan(LeafNode):
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    def eval(self, file):
        file_size = os.path.getsize(file)
        return file_size > self._limit


class SuffixIs(LeafNode):
    def __init__(self, suffix):
        super().__init__()
        self._suffix = suffix

    def eval(self, file):
        suffix = file.split('.')[-1]
        return self._suffix == suffix


class NonLeafNode(TreeNode):
    def __init__(self, op, left, right) -> bool:
        self._op = op
        self._left = left
        self._right = right
        self._is_leaf = False

    def is_leaf(self):
        return False

    def eval(self, file):
        if self._op == 'and':
            return self._left.eval(file) and self._right.eval(file)
        elif self._op == 'or':
            return self._right.eval(file) or self._right.eval(file)


def filter_file(file, predicates: TreeNode) -> bool:
    return predicates.eval()


gt = GreaterThan(100)
suffixIsJpg = SuffixIs("jpg")
andPredicate = NonLeafNode('and', gt, suffixIsJpg)

print('Running tests')
print("assert(gt.is_leaf())")
assert(gt.is_leaf())
print('assert(not gt.eval("predicate_test.jpg"))')
assert(not gt.eval("predicate_test.jpg"))
print('assert(suffixIsJpg.eval("test.jpg"))')
assert(suffixIsJpg.eval("test.jpg"))
assert(not andPredicate.eval("predicate_test.jpg"))
print("Done with tests")

