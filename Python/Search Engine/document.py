"""
Non Pronanun
CSE 163 AD

This is the file for the Document class, it's job is to read the files
and create the frequency of the terms. It can also return the different
characteristics of the file according to the methods.
"""


from cse163_utils import normalize_token


class Document:
    """
    Represents a Document with it's file path, wordcount and a
    storage for the frequency of each of the words in the file.
    """
    def __init__(self, file_path: str) -> None:
        """
        Initializes the Document object with the file path, counts
        the words in the file and calculates the term frequency
        of each of the word, given by the formula count of term
        divided by count of words, which is stored in a dictionary.
        """
        self._path: str = file_path
        self._wordcount: int = 0
        self._frequency: dict[str, int] = {}
        with open(file_path) as f:
            text = f.read()
            words = text.split()
            for word in words:
                word = normalize_token(word)
                if word not in self._frequency:
                    self._frequency[word] = 0
                self._frequency[word] += 1
            self._wordcount = len(words)
        for word in self._frequency.keys():
            self._frequency[word] /= self._wordcount

    def term_frequency(self, term: str) -> float:
        """
        This method takes in a term and finds the frequency
        of the term within the Document file, it returns zero
        if the word doesn't exist in the file. The case and the
        punctuation doesn't matter in this function.
        """
        term = normalize_token(term)
        if term in self._frequency:
            return self._frequency[term]
        else:
            return 0

    def get_path(self) -> str:
        """
        This returns the file path of current Document object.
        """
        return self._path

    def get_words(self) -> list[str]:
        """
        This returns a list of all unique words in the Document file.
        """
        return list(self._frequency.keys())

    def __str__(self) -> str:
        """
        gives a brief summary of the Document, with its path and its
        wordcount.
        """
        return "Document(" + self._path + ", words: " \
               + str(self._wordcount) + ")"