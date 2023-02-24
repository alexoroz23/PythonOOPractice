"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """Machine for finding random words from dictionary.

    Args:
    path (str): A string representing the path to the file containing the words.

    Attributes:
    words (list): A list containing all the words read from the dictionary file.

    Methods:
    parse: Parses the dictionary file and returns a list of words.
    random: Returns a random word from the list of words.

    Example:
    >>> wf = WordFinder("simple.txt")
    3 words read
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words.

        Args:
        dict_file (file): A file object representing the dictionary file.

        Returns:
        list: A list of words parsed from the dictionary file.
        """

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word.

        Returns:
        str: A random word from the list of words.
        """

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    Inherits from:
    WordFinder

    Methods:
    parse: Overrides the parse method in WordFinder to exclude blank lines and comments.

    Example:
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read
    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments.

        Args:
        dict_file (file): A file object representing the dictionary file.

        Returns:
        list: A list of words parsed from the dictionary file, with blank lines and comments excluded.
        """

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]