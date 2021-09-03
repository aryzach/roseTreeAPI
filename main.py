

class RoseTree:
    """
    // depth 0
    >>> a=RoseTree(5)
    >>> b=RoseTree(10)
    >>> c=RoseTree(100)
    >>> d=RoseTree(2)
    >>> e=RoseTree(4)
    >>> f=RoseTree(8)

    // depth 1
    >>> ab = RoseTree(1, [a,b])

    // depth 2
    >>> abca = RoseTree(1, [ab,c,a])

    // depth 3
    >>> ababcaa = RoseTree(1, [ab,abca,a])

    >>> a.get_value()
    5
    >>> ab.get_value_at()
    5
    >>> ab.get_value_at([0])
    5

    """
    def __init__(self, value, subtrees=[]):
        self.value = value 
        self.subtrees = subtrees

    def get_value(self):
        return self.value

    def get_value_at(self, list_path_to_target=[]):
        return False




if __name__ == "__main__":
    import doctest
    doctest.testmod()
