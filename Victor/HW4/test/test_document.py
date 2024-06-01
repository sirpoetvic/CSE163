"""
CSE 163: HW4 Part 0 - Subset of Tests
Original Author: Joshua L Ervin
Modified by: Jeff Stride
"""

import unittest
import re
from document import Document as DocumentStudent


class TestPart0(unittest.TestCase):
    """Tests for hw4, part 0"""

    def setUp(self):
        self._test_file = 'test_corpus\\document1.txt'
        self._test_file_long = 'test_corpus\\nsa.txt'
        self._student = DocumentStudent(self._test_file)
        self._student_long = DocumentStudent(self._test_file_long)
        # self.process_test_tags()

    def process_test_tags(self):
        p = re.compile('#name\((.*)\)')
        test_name = p.findall(self._testMethodDoc)
        if test_name:
            print(test_name[0])
            
    def test_p0_get_words_term_freq(self):
        """
        #name([Behavior: Common Case] D0: Testing document get_words and term_frequency have the same values)
        """
        msg = "Testing document get_words and term_frequency in document1.txt file"
        student_words = sorted(self._student.get_words())
        sol_words = ['bruno', 'i', 'love']
        self.assertEqual(sol_words, student_words, msg)
        sol_freq = [ 1/3, 1/3, 1/3 ]
        for word, freq in zip(student_words, sol_freq):
            self.assertAlmostEqual(self._student.term_frequency(word),
                                   freq,
                                   delta=0.001,
                                   msg=msg)

    def test_p0_term_freq_zero_return(self):
        """
        #name([Behavior: Edge Case] D1: Testing document term_frequency, returns zero)
        """
        msg = 'Testing term_frequency on document1, zero return'
        sol = self._student.term_frequency('potato')
        self.assertTrue(sol == 0, msg=msg)

    def test_p0_term_freq_zero_return_long(self):
        """
        #name([Behavior: Edge Case] D2: Testing document term_frequency on long file, returns zero)
        """
        # msg = 'Testing compute_frequencies on nsa.txtc, zero return'
        sol = self._student_long.term_frequency('asdfasdf')
        self.assertTrue(sol == 0)

    def test_p0_term_freq_long(self):
        """
        #name([Behavior: Edge Case] D3: Testing document term_frequency nsa.txt, ignore cases and punctuation)
        """
        msg = 'Testing compute_frequencies on nsa.txt'
        term = 'coLleCtion...'
        sol = self._student_long.term_frequency(term)
        ans = 0.00871459
        self.assertAlmostEqual(sol, ans, delta=0.001, msg=msg)

    def test_p0_compute_freq_long(self):
        """
        #name([Behavior: Common Case] D4: Testing get_words and term_frequency have same values)
        """
        msg = 'Testing document can use get_words followed by term_frequency'
        student_words = sorted(self._student_long.get_words())
        sol_words = ['1952', '2013', 'a', 'ability', 'accomplish', 'according', 'across', 'actions', 
        'activities', 'agency', 'agencys', 'alleged', 'allegedly', 'alongside', 'also', 'and', 
        'antivietnamwar', 'are', 'as' ]
        self.assertEqual(sol_words, student_words[:19], msg)
        sol_freq = [0.00217, 0.00217, 0.02178, 0.00217, 0.00217, 0.00217, 0.00217, 0.00217, 0.00217, 
          0.01089, 0.00217, 0.00217, 0.00217, 0.0021, 0.00653, 0.03267, 0.00217, 0.00435, 0.01960]
        for word, freq in zip(sol_words, sol_freq):
            self.assertAlmostEqual(self._student_long.term_frequency(word),
                                   freq,
                                   delta=0.0001,
                                   msg=msg)
        
    def test_get_words_returns_list(self):
        """
        #name([Behavior: Common Case] D5: Tests whether get_words returns a list)
        """
        words = self._student.get_words()
        self.assertTrue(isinstance(words, list))