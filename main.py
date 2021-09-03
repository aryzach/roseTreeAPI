


class RoseTree:
    """
    >>> a=RoseTree(5)
    >>> a.get_value()
    5
    """
    def __init__(self, value, subtrees=[]):
        self.value = value 
        self.subtrees = subtrees

    def get_value(self):
        return self.value



if __name__ == "__main__":
    import doctest
    doctest.testmod()
