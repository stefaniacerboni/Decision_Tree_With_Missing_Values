class DecisionLeaf:
    """A leaf of a decision tree holds just a result."""

    def __init__(self, result):
        self.result = result

    def __call__(self, example):
        return self.result

    def display(self, indent=0):
        print(' ' * 4 * indent, 'RESULT =', self.result)

    def __repr__(self):
        return repr(self.result)
