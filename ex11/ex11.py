#################################################################
# FILE : ex11.py, EXERCISE : intro2cse ex11 2021
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb, 212017719
# DESCRIPTION : A simple program that represents classes to build decision tree
#################################################################
import itertools
from collections import Counter


class Node:
    """Class that represents the Node object."""

    def __init__(self, data, positive_child=None, negative_child=None):
        """
        :param data: The data for node.
        :param positive_child: The left child of the node.
        :param negative_child: The right child of the node.
        """
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def __eq__(self, other):
        """
        A method that checks if two nodes are equal along the tree, using a
        helper function.
        :param other: Another node object.
        :return: True if self and other are the same, False else.
        """
        return check(self, other)

    def this_node_leaf(self):
        """A method that returns if a node is leaf (its children are None)"""
        return self.negative_child is None and self.positive_child is None


def check(n1, n2):
    """A helper function that returns True if two nodes are equal."""
    if n1.this_node_leaf() and n2.this_node_leaf() and n1.data == n2.data:
        return True
    elif n1.data != n2.data:
        return False
    return check(n1.negative_child, n2.negative_child) and check(
        n1.positive_child, n2.positive_child)


class Record:
    """Class that represents the Record object."""

    def __init__(self, illness, symptoms):
        """
        :param illness: An illness.
        :param symptoms: The symptoms of the illness.
        """
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    A function that loads the data from the file in Record objects.
    :param filepath: The name of the file.
    :return: A list of the illnesses records.
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """Class that represents the Diagnoser object."""

    def __init__(self, root):
        """
        :param root: The root of the tree.
        """
        self.root = root

    def diagnose(self, symptoms):
        """A method that finds the suitable illness for symptoms, using a
        helper function. Saves the root at first, then searches the tree."""
        root_save = self.root  # Saves the root.
        return_diagnose = self.__diagnose_helper(symptoms, self.root)
        self.root = root_save
        return return_diagnose

    def __diagnose_helper(self, symptoms, r):
        """
        A helper function that finds the suitable illness, reaching the leaves,
        by calling the method diagnose.
        :param symptoms: A list of symptoms.
        :param r: The current node.
        :return: The suitable illness.
        """
        if r.this_node_leaf():  # If it is a leaf return its data.
            return r.data
        if r.data in symptoms:  # If the current data is in the list (Yes).
            self.root = r.positive_child
        else:  # The answer is (No).
            self.root = r.negative_child
        return self.diagnose(symptoms)

    def calculate_success_rate(self, records):
        """
        A method that calculates the success rate of Records.
        :param records: A list of Record objects.
        :return: The success rate.
        """
        if not records:  # If the list is empty don't calculate the rate.
            raise ValueError("The List is empty.")
        illness_count = 0
        for r in records:
            if r.illness == self.diagnose(r.symptoms):
                illness_count += 1
        return illness_count / len(records)  # Calculate the rate.

    def all_illnesses(self):
        """
        A method that finds the illnesses in a tree, using a helper function.
        :return: Sorted list of the illnesses if they aren't None.
        """
        illnesses_lst = []
        self.__illnesses_helper(self.root, illnesses_lst)
        remove_tup_lst = []
        if illnesses_lst:
            illnesses_lst = Counter(illnesses_lst).most_common()
            # Remove the second element from tuples.
            for r in illnesses_lst:
                remove_tup_lst.append(r[0])
        return remove_tup_lst

    def __illnesses_helper(self, r, illnesses_lst):
        """
        A helper function that puts the illnesses is a list.
        :param r: The current node, first it's the tree root.
        :param illnesses_lst: The return list, first it's empty.
        :return: A list of all the illnesses.
        """
        if r is not None:  # Checks if the node is None.
            self.__illnesses_helper(r.negative_child, illnesses_lst)
            self.__illnesses_helper(r.positive_child, illnesses_lst)
            if r.data is not None and r.this_node_leaf():  # It's an illness
                illnesses_lst.append(r.data)
                return

    def paths_to_illness(self, illness):
        """
        A method that finds all the paths to some illness, using a helper
        function.
        :param illness: An illness.
        :return: A list of all the paths to this illness (list of lists).
        """
        paths_lst = []  # The list of the paths.
        self.__paths_helper(illness, self.root, [], paths_lst)
        return paths_lst

    def __paths_helper(self, illness, node, path, paths_lst):
        """
        A helper function that finds the paths.
        :param illness: An illness.
        :param node: The current node, first it's empty.
        :param path: The current path, we start it empty at first.
        :param paths_lst: The return list, first it's empty.
        :return: A list of all the paths to this illness (list of lists).
        """
        if node is None:  # Check the node is None.
            return
        if node.this_node_leaf():
            if node.data == illness:
                paths_lst.append(path)  # We find the illness, append its path.
        # Try with True then try with False.
        temp_path = path + [True]
        self.__paths_helper(illness, node.positive_child, temp_path, paths_lst)
        temp_path = path + [False]
        self.__paths_helper(illness, node.negative_child, temp_path, paths_lst)

    def minimize(self, remove_empty=False):
        """A method that minimizes a tree according to the remove_empty's
        value, using a helper function."""
        self.root = self.__minimize_helper(self.root, remove_empty)

    def __minimize_helper(self, n, rem):
        """
        A helper function that removes duplications and Nones according to rem.
        :param n: The current value, first it's the root.
        :param rem: Boolean value.
        :return: The minimized tree.
        """
        if not n.this_node_leaf():
            # Two calls to reach each leaf in the tree first.
            neg_tree = self.__minimize_helper(n.negative_child, rem)
            pos_tree = self.__minimize_helper(n.positive_child, rem)
            n = decide_what_to_return(neg_tree, pos_tree, rem, n)
        return n


def decide_what_to_return(neg, pos, rem, cur_n):
    """A helper function that decides which subtree to return."""
    if rem is True:  # Remove Nones if True.
        if neg.data is None:
            return pos
        if pos.data is None:
            return neg
    n = pos if pos == neg else Node(cur_n.data, pos, neg)  # Remove duplication
    return n


def build_tree(records, symptoms):
    """A function that builds a decision tree according to records and
    symptoms lists, after checking the types, using a helper function."""
    # If exception found this function raises it.
    raise_exception1(records, symptoms)
    if not symptoms:  # Find the most common illness in records list.
        illness_node = find_suitable([], [], records)
        return Diagnoser(illness_node)
    # Take the first symptom, make it the root, then build tree with helper.
    n = Node(symptoms[0])
    symptoms_index = 1
    build_helper(records, symptoms, n, [], [], symptoms_index)
    return Diagnoser(n)  # Return the Tree.


def build_helper(records, symptoms, n, pos, neg, symptom_index):
    """
    A helper function that builds the tree, at the end it finds the suitable
    illnesses, using helper functions.
    :param records: A list of Record object.
    :param symptoms: A list of symptoms.
    :param n: The current node, first it contains the first symptom (root).
    :param pos: A list of the symptoms that answers yes, for each path.
    :param neg: A list of the symptoms that answers no, for each path.
    :param symptom_index: An index for symptoms list.
    :return: None.
    """
    cur = n.data
    if symptom_index != len(symptoms):
        build_tree_path_add(symptoms, symptom_index, n, records, pos, neg, cur)
    else:  # Reaches the end of the list -> Find suitable illnesses.
        build_tree_path_end(pos, neg, cur, records, n)


def build_tree_path_add(symptoms, i, n, records, pos, neg, cur):
    """ A helper function that adds symptoms to the tree and call the func."""
    current_symptom = symptoms[i]
    n.negative_child = Node(current_symptom)
    build_helper(records, symptoms, n.negative_child, pos, neg + [cur], i + 1)
    n.positive_child = Node(current_symptom)
    build_helper(records, symptoms, n.positive_child, pos + [cur], neg, i + 1)


def build_tree_path_end(pos_lst, neg_lst, cur, records, n):
    """ A helper function that adds illness to the end of every path."""
    # Call find_illness for Yes and No!
    n.negative_child = find_suitable(pos_lst, neg_lst + [cur], records)
    n.positive_child = find_suitable(pos_lst + [cur], neg_lst, records)


def find_suitable(pos_lst, neg_lst, records):
    """A helper function that finds the suitable illness from the records list.
    It sets the (Yes) answers list and checks if it is a subset of the illness
    symptoms, then checks if all symptoms aren't in the (No) list, so this is
    a suitable illness. It returns a Node of the most common illness."""
    positive_set = set(pos_lst)  # Set the positive list.
    illnesses = []  # A list that contains all the suitable illnesses.
    for record in records:
        if positive_set.issubset(set(record.symptoms)):
            if is_it_suitable(record.symptoms, neg_lst):
                illnesses.append(record.illness)
    if not illnesses:  # None illness if empty
        return Node(None)
    illnesses = Counter(illnesses).most_common()
    return Node(illnesses[0][0])  # return the most common illness in the list.


def is_it_suitable(symptoms, negative_lst):
    """A helper function that checks if there is intersection in 2 lists."""
    for symptom in negative_lst:
        if symptom in symptoms:
            return False
    return True


def optimal_tree(records, symptoms, depth):
    """A function that gets list of records, list of symptoms and some depth.
    It returns the highest success rated tree, using a helper function."""
    # If exceptions found this function or build_tree function raise them.
    raise_exception2(depth, symptoms)
    return_tree, max_rate = Diagnoser(Node(None)), 0
    return optimal_helper(records, symptoms, depth, max_rate, return_tree)


def optimal_helper(records, symptoms, depth, max_rate, return_tree):
    """A helper function that updates return_tree to the max success rated"""
    for comp in itertools.combinations(symptoms, depth):
        tree = build_tree(records, comp)
        success_rate_for_tree = tree.calculate_success_rate(records)
        if success_rate_for_tree >= max_rate:
            return_tree, max_rate = tree, success_rate_for_tree  # Set results.
    return return_tree


def raise_exception1(records_lst, symptoms_lst):
    """A function that raises an exception if there is a TypeError."""
    for record in records_lst:
        if not isinstance(record, Record):
            raise TypeError("Found a nonRecord element in records list.")
    for symptom in symptoms_lst:
        if not isinstance(symptom, str):
            raise TypeError("Found a nonstring element in symptoms list.")


def raise_exception2(depth, symptoms_lst):
    """A function that raises an exception if there is a ValueError."""
    if not 0 <= depth <= len(symptoms_lst):
        raise ValueError("Invalid depth value.")
    symptoms_set = set(symptoms_lst)
    if len(symptoms_set) != len(symptoms_lst):
        raise ValueError("Found double symptoms.")


if __name__ == "__main__":
    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)
    diagnoser = Diagnoser(root)
    # Simple test for 1:
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)
    # Simple test for 2:
    try:
        rate = diagnoser.calculate_success_rate([])
        print("The success rate is: " + str(rate))
    except ValueError:
        print("You should call it with a nonempty list.")
    # Simple tests for 3:
    print("Print the illnesses for diagnoser:", end=" ")
    print(diagnoser.all_illnesses())
    # Simple tests for 4:
    print("One path for cold: True -> False:", end=" ")
    print(diagnoser.paths_to_illness("cold"))  # One path: True -> False
    print("No paths for None in diagnoser:", end=" ")
    print(diagnoser.paths_to_illness(None))  # No paths for None.
    a = Node("cold")
    s = Diagnoser(a)
    print("One path to illness in root ->", end=" ")
    print(s.paths_to_illness("cold"))
    k = Diagnoser(None)
    print("No paths in None root ->", end=" ")
    print(k.paths_to_illness("inf"))
    # Simple tests for 5:
    r1 = Record("cold", ["fever"])
    r2 = Record("healthy", [])
    try:
        di = build_tree([r1, r2], ["fever"])
        if di.root.data == "fever" and di.root.positive_child.data == "cold" \
                and di.root.negative_child.data == "healthy":
            print("Test passed.")
        else:
            print("The test didn't pass.")
    except TypeError:
        print("Call the function with right types.")
    # Simple tests for 6:
    r1 = Record("cold", ["fever"])
    r2 = Record("influenza", ["fever", "cough"])
    try:
        di = optimal_tree([r1, r2], ["fever", "cough"], 1)
        if di.root.data == "cough" and di.root.negative_child.data == "cold" \
                and di.root.positive_child.data == "influenza":
            print("Test passed.")
        else:
            print("The test didn't pass.")
    except TypeError:
        print("Call the function with right types")
    except ValueError:
        print("Call the function with valid depth and symptoms.")
