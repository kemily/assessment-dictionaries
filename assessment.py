"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # creating an empty dictionary
    word_count = {}

    # creating a list of words from the input phrase by using .split() method
    words = phrase.split()

    # iterating over the words list and assigning a word as a key and it's count
    # as it's value to the dictionary word_counts
    # if a word key isn't in dictionary we'll assign it to it and 0
    # as it's initial value, if it does we'll increase the count value by 1
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # created a dictionary melons with melon names as keys and prices as values
    melons = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25
    }

    # checks if the input melon name is not in the melons dictionary
    # if it's not returns "No price found"
    if melon_name not in melons:
        return "No price found"

   # returns a price of the input melon name from the dictionary
    return melons[melon_name]


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # creating an empty dictionary word_length
    word_length = {}

    # iterating over the words list to set dictionary key value pairs
    # key is the length of words and value  - the list of words by length
    # if dictionary doesn't have word length key .setdefault() method will set it
    # and will assign an empty list to it.
    # If it has - a word will be append to the value list, base on the word length.
    for word in words:
        word_length.setdefault(len(word), []).append(word)

    # looping over the keys and values of the dictionary by using .items() method
    # and updating the list value of the dictionary to be sorted
    for length, value in word_length.items():
        word_length[length] = sorted(value)

    # .items() method returns a list of tuples of the key value pairs
    return word_length.items()


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # creating pirate_translations dictionary with English to Pirate translations
    pirate_translations = {
                "sir": "matey",
                "hotel": "fleabag inn",
                "student": "swabbie",
                "man": "matey",
                "professor": "foul blaggart",
                "restaurant": "galley",
                "your": "yer",
                "excuse": "arr",
                "students": "swabbies",
                "are": "be",
                "restroom": "head",
                "my": "me",
                "is": "be"
    }

    # defining an empty list to store the translation
    pirate_talk = []

    # splitting the input phrase into the list of words
    phrase_words = phrase.split()

    # iterating over the phrase words and checking if the pirate_translations
    # dictionary has these words to translate them into Pirate words.
    # the resuilt will be appended to the pirate_talk list
    for word in phrase_words:
        if word not in pirate_translations:
            pirate_talk.append(word)
        else:
            pirate_talk.append(pirate_translations[word])

    # return the Pirate translation by joining the pirate_talk list words into a phrase
    return " ".join(pirate_talk)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
   
   # Couldn't resolve this problem
    

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
