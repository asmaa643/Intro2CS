#################################################################
# FILE : ex3.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex3 2021
# DESCRIPTION: A simple program that has different required functions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: I used some help functions to simplify else functions.
#################################################################

def input_list():
    """
    This function gets numbers as inputs, orders them in list, sums them in
    the last item and returns it
    """
    my_list = list()
    list_sum = 0
    x = input()
    while x:
        my_list.append(float(x))
        list_sum += float(x)
        x = input()
    my_list.append(list_sum)
    return my_list


def inner_product(vec_1, vec_2):
    """
    This function gets 2 lists of numbers that have the same length of items
    and returns the standard inner product of the numbers
    """
    if len(vec_1) != len(vec_2):
        return None
    if len(vec_1) == 0:
        return 0
    sum_vec = 0
    for i in range(len(vec_1)):
        sum_vec += vec_1[i]*vec_2[i]
    return sum_vec


def is_ascending(lst):
    """ This function gets a list and checks if it is ascending or not """
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
    return True


def is_descending(lst):
    """ This function gets a list and checks if it is descending or not """
    for i in range(len(lst)-1):
        if lst[i+1] > lst[i]:
            return False
    return True


def is_there_equal(lst):
    """
    This function gets a list and checks if it has at least two equal sequence
    items or not
    """
    for i in range(len(lst)-1):
        if lst[i+1] == lst[i]:
            return True
    return False


def is_all_equal(lst):
    """ This function gets a list and checks if all the items are equal """
    for i in range(len(lst)-1):
        if lst[i+1] != lst[i]:
            return False
    return True


def sequence_monotonicity(sequence):
    """
    This function gets a list of numbers and returns a list of its sequence
    monotonicity (according to the definition)
    """
    lst = [True, True, True, True]
    if len(sequence) == 0 or len(sequence) == 1:
        return lst
    elif is_all_equal(sequence):
        lst[1], lst[3] = False, False
    elif is_ascending(sequence):
        lst[2], lst[3] = False, False
        if is_there_equal(sequence):
            lst[1] = False
    elif is_descending(sequence):
        lst[0], lst[1] = False, False
        if is_there_equal(sequence):
            lst[3] = False
    else:
        lst = [False, False, False, False]
    return lst


def monotonicity_inverse(def_bool):
    """ This function gets a list of some sequence monotonicity and returns a
    list that show an example for it """
    if def_bool == [False, False, False, False]:
        return [1, 2, 1, 2]
    elif def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    elif def_bool == [True, False, False, False]:
        return [1, 2, 2, 4]
    elif def_bool == [False, False, True, True]:
        return [4, 3, 2, 1]
    elif def_bool == [False, False, True, False]:
        return [4, 3, 2, 2]
    elif def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    else:
        return None


def is_prime(num):
    """
    This function gets a number > 1 and returns if it is a prime number or not
    """
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, int(num**0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True


def primes_for_asafi(n):
    """
    This function gets a number (n) and returns the first primes numbers in the
    range of 2 and n
    """
    primes_list = list()
    primes_count = 0
    current_num = 2  # No need to check numbers below 2, so start with 2.
    while primes_count < n:
        if is_prime(current_num):
            primes_list.append(current_num)
            primes_count += 1
        current_num += 1
    return primes_list


def sum_of_vectors(vec_lst):
    """
    This function gets a list of vectors and returns a list of the vectors' sum
    """
    if len(vec_lst) == 0:
        return None
    lists_len = len(vec_lst[0])
    vec_sum_lst = []
    if lists_len == 0:
        return vec_sum_lst
    for i in range(lists_len):
        vec_sum_lst.append(0)
    for i in range(len(vec_lst)):
        for j in range(lists_len):
            vec_sum_lst[j] += vec_lst[i][j]
    return vec_sum_lst


def num_of_orthogonal(vectors):
    """
    This function gets a list of vectors, counts the pairs of perpendicular
    vectors and returns the number.
    """
    zero_inner_products = 0
    i = 0
    while i < len(vectors)-1:
        j = i + 1
        while j < len(vectors):
            if inner_product(vectors[i], vectors[j]) == 0:
                zero_inner_products += 1
            j += 1
        i += 1
    return zero_inner_products
