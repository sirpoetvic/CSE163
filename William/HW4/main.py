# Author Dylan Jergens
# This program runs the search engine, taking user input

from search_engine import SearchEngine
import unittest

def main():
    print('Welcome to 6oog13!!')
    directory = input('Please enter a the name of a directory: ')

    print('Building Search Engine...')
    print()
    engine = SearchEngine(directory)

    answer = 'y'
    while (answer == 'y'):
        term = input('Search (enter a term to query): ')
        ranking = engine.search(term)
        print("Displaying results for " + "'" + term + "':")
        if ranking is None or len(ranking) == 0:
            print('    No results :(')
        else:
            rank = 1
            for doc in ranking:
                print('    ' + str(rank) + '. ' + doc)
                rank += 1
            print()
        answer = ''
        while not (answer == 'y' or answer == 'n'):
            answer = input('Would you like to search another term (y/n) ')

def run_tests():
    test_loader = unittest.TestLoader()
    tests = test_loader.discover("test")
    test_runner = unittest.runner.TextTestRunner()
    result = test_runner.run(tests)
    
if __name__ == '__main__':
    main()
