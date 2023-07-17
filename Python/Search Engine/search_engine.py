"""
Non Pronanun
CSE 163 AD

This is the testing file for Document and SearchEngine.
"""


from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine
# from search_engine import SearchEngine


# Define your test functions here!
def test_Document() -> None:
    """
    These are the test cases for Document
    """
    document = Document("/course/small_wiki/William McKinley - Wikipedia.html")
    assert_equals("/course/small_wiki/William McKinley - Wikipedia.html",
                  document.get_path())
    document2 = Document("/home/Corgi.txt")
    assert_equals("/home/Corgi.txt", document2.get_path())
    assert_equals(['corgi', 'pembroke', 'welsh', 'corgis', 'cutest', 'dog',
                  'since', 'the', '12th', 'century'], document2.get_words())
    assert_equals("Document(/course/small_wiki/William McKinley"
                  " - Wikipedia.html, words: 34599)", str(document))
    assert_equals(0.25, document2.term_frequency("corgi"))
    assert_equals("Document(/home/Corgi.txt, words: 12)", str(document2))


def test_search_engine() -> None:
    """
    These are the test cases for SearchEngine
    """
    search_test = SearchEngine("/home/test_files")
    assert_equals("SearchEngine(/home/test_files, size: 3)", str(search_test))
    assert_equals([], search_test.search("Non"))
    assert_equals(['/home/test_files/dog2.txt', '/home/test_files/dog.txt'],
                  search_test.search("corgi"))
    assert_equals(['/home/test_files/dog2.txt', '/home/test_files/dog3.txt',
                  '/home/test_files/dog.txt'], search_test.search("corgi and"))


def main() -> None:
    # Call your test functions here!
    test_Document()
    test_search_engine()


if __name__ == '__main__':
    main()