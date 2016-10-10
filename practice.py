"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # setting an empty list no_duplicates
    # if we passing an empty list to the function it will return this list,
    # which is empty
    no_duplicates = []

    # we assign a set of the passed into the function list to a variable words_set
    # it will store all the unique elements from the list, without the duplicates
    words_set = set(words)

    # creating a list of the unique elements from the set and assigning it to the no_duplicates
    no_duplicates = list(words_set)

    return no_duplicates


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # we assign sets of the passed into the function lists to a variables items1_set
    # and items2_set respectively
    items1_set = set(items1)
    items2_set = set(items2)

    # creating a list of the unique common items by using Set Math between our two
    # created sets. So it will return an intersection of unique elements, that these
    # two set have in common.
    unique_common_items = list(items1_set & items2_set)

    return unique_common_items


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0."""

    # creating an empty list, where we'll store our pairs
    sum_zero_pairs = []

    #creating a list of unique numbers by using set of imput numbers list
    unique_numbers = list(set(numbers))

    #tried to do dictionary comprehension, sublime throws an error -->
    # --> numbers_dict = {number: unique_numbers for number in unique_numbers}

    # created a dictionary, where key is each unique list number and it's value
    # is the whole unique numbers list
    numbers_dict = {}
    for number in unique_numbers:
        numbers_dict[number] = unique_numbers

    # accessing dictionary's keys and value lists by using method .items()
    # and iterating over it's value lists by index
    # if sum of item and one of it's list elemets equals 0 AND also a list of
    # them as elemets is not in the sum_zero_pairs list,
    # then we sort a list of these two values and append them to the sum_zero_pairs list
    for item, value_numbers in numbers_dict.items():
        for i in range(len(value_numbers)):
            if item + value_numbers[i] == 0 and [item, value_numbers[i]] not in sum_zero_pairs:
                key_value = sorted([item, value_numbers[i]])
                sum_zero_pairs.append(key_value)

    return sum_zero_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    # creating an empty list, where we'll store our chars
    top_char = []

    # defining a dictionary where we'll store our character count data
    letter_count = {}

    # iterating over the phrase, choosing only alphabetical characters to assign
    # to the dictionary as a key and their count as a value
    for letter in phrase:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # creating a list of all count values from the dictionary by using .value() method
    counts = letter_count.values()

    # choosing a max number of character counts in the counts list
    max_count = max(counts)

    # iterating over the dictionary
    # if character count value is equals to the max count we'll append that character
    # to the empty list top_char
    for char in letter_count:
        if letter_count[char] == max_count:
            top_char.append(char)

    return sorted(top_char)

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
