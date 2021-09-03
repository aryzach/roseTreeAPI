

class RoseTree:
    """
    add composite / class level tests here
    """
    def __init__(self, value, subtrees=[]):
        self.value = value 
        self.subtrees = subtrees

    def get_value(self):
        """
        >>> a.get_value()
        5
        """
        return self.value

    def get_value_at(self, list_path_to_target=[]):
        """
        >>> abca.get_value_at()
        2
        >>> abca.get_value_at([0])
        1
        >>> ababcaa.get_value_at([0])
        1
        >>> ababcaa.get_value_at([1,2])
        5
        """
        if list_path_to_target == []:
            return self.get_value()
        else:
            # use try / except
            # could I use tail recursion here?
            first_subtree, *rest_of_path = list_path_to_target
            return self.subtrees[first_subtree].get_value_at(rest_of_path)
            





if __name__ == "__main__":
    # depth 0
    a = RoseTree(5)
    b = RoseTree(10)
    c = RoseTree(100)
    d = RoseTree(2)
    e = RoseTree(4)
    f = RoseTree(8)

    # depth 1
    ab = RoseTree(1, [a,b])

    # depth 2
    abca = RoseTree(2, [ab,c,a])

    # depth 3
    ababcaa = RoseTree(7, [ab,abca,a])


    import doctest
    doctest.testmod(extraglobs={
        'a'       : a,
        'b'       : b,
        'c'       : c,
        'd'       : d,
        'e'       : e,
        'f'       : f,
        'ab'      : ab, 
        'abca'    : abca,
        'ababcaa' : ababcaa 
        })
