import copy

class RoseTree:
    """
    add composite / class level tests here
    """
    def __init__(self, value, subtrees=[]):
        self.value = value 
        self.subtrees = subtrees


    def equal_by_value(self, rosetree):
        """
        >>> a.equal_by_value(a)
        True
        >>> a.equal_by_value(b)
        False
        >>> ababcaa.equal_by_value(b)
        False
        >>> ababcaa.equal_by_value(ababcaa)
        True
        """
        top_level_equal = self.get_value() == rosetree.get_value()
        subtrees_equal = True
        # this could be reduce / code that short circuits on False
        for i in range(len(self.subtrees)):
            if len(self.get_subtrees()) != len(rosetree.get_subtrees()):
                return False
            elif self.get_subtrees()[i].equal_by_value(rosetree.get_subtrees()[i]):
                pass
            else:
                subtrees_equal = False
        return top_level_equal and subtrees_equal

    def get_subtrees(self):
        return self.subtrees

    def get_value(self):
        """
        >>> a.get_value()
        5
        """
        return self.value

    def get_value_at(self, list_path_indexes_to_target=[]):
        """
        >>> abca.get_value_at()
        2
        >>> abca.get_value_at([0])
        1
        >>> ababcaa.get_value_at([0])
        1
        >>> ababcaa.get_value_at([1,2])
        5
        >>> abca.get_value_at([1,2,3])
        that rose path doesn't exist
        """
        if list_path_indexes_to_target == []:
            return self.get_value()
        else:
            # could I use tail recursion here?
            try:
                first_subtree_index, *rest_of_path_indexes = list_path_indexes_to_target
                return self.subtrees[first_subtree_index].get_value_at(rest_of_path_indexes)
            except IndexError:
                print("that rose path doesn't exist")

    def replace_value(self, new_value):
        """
        >>> ababcaa.replace_value(6).get_value()
        6
        >>> ababcaa.replace_value(8).equal_by_value(RoseTree(8, [ab,abca,a]))
        True
        """
        self.value = new_value
        return self 

    def replace_value_at(self, new_value, list_path_indexes_to_target=[]):
        """
        >>> a.replace_value_at(0).get_value()
        0
        >>> a.replace_value_at(0).equal_by_value(RoseTree(0))
        True
        >>> ababcaa.replace_value_at(3, [1,0]).get_value_at([1,0])
        3
        >>> abca.replace_value_at(30, [1,2,3]).equal_by_value(abca)
        that rose path doesn't exist
        True
        """
        try:
            if list_path_indexes_to_target == []:
                self.replace_value(new_value)
            else:
                first_subtree_index, *rest_of_path_indexes = list_path_indexes_to_target
                self.get_subtrees()[first_subtree_index].replace_value_at(new_value, rest_of_path_indexes)
        except IndexError:
            print("that rose path doesn't exist")
        finally:
            return self

    # list_path_indexes_to_target must be exact path
    def insert_tree_at(self, tree, list_path_indexes_to_target):
        """
        >>> copy.deepcopy(a).insert_tree_at(a, [0]).equal_by_value(RoseTree(5, [a])) 
        True
        >>> copy.deepcopy(a).insert_tree_at(a, [9]).equal_by_value(RoseTree(5, [a])) 
        True
        >>> copy.deepcopy(ababcaa).insert_tree_at(b, [2]).equal_by_value(RoseTree(7, [ab,abca,b]))
        True
        >>> copy.deepcopy(ababcaa).insert_tree_at(b, [1]).equal_by_value(RoseTree(7, [ab,b,a]))
        True
        >>> copy.deepcopy(ababcaa).insert_tree_at(a, [1,1]).equal_by_value(RoseTree(7, [ab,RoseTree(2, [ab,a,a]),a]))
        True
        >>> copy.deepcopy(ababcaa).insert_tree_at(ababcaa, [1,1]).equal_by_value(RoseTree(7, [ab,RoseTree(2, [ab,ababcaa,a]),a]))
        True
        >>> copy.deepcopy(abca).insert_tree_at(a, [1,2,3]).equal_by_value(abca)
        that rose path doesn't exist
        True

        """
        try:
            if list_path_indexes_to_target == []:
                print("need to specify a rose location")
                return self
            elif len(list_path_indexes_to_target) == 1:
                spec_position = list_path_indexes_to_target[0]
                subtrees_size = len(self.get_subtrees())
                if spec_position >= subtrees_size:
                    self.subtrees.append(tree)
                else:
                    self.subtrees[spec_position] = tree
            else:
                first_subtree_index, *rest_of_path_indexes = list_path_indexes_to_target
                self.get_subtrees()[first_subtree_index].insert_tree_at(tree, rest_of_path_indexes)
        except IndexError:
            print("that rose path doesn't exist")
        finally:
            return self



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
    doctest.IGNORE_EXCEPTION_DETAIL
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
