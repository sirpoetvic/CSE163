# A file that contains some CSE 163 specific helper functions
# You do not need to understand how these functions are implemented,
# but you should be able to use the ones we described in class!


import math
import pandas as pd

def series_equals(s1, s2):
    # verify lengths are the same
    if len(s1) != len(s2):
        return False
    # verify that each has the same set of indices
    indices_good = all([idx1 == idx2 for idx1, idx2 in zip(s1.index, s2.index)])
    if not indices_good:
        return False
    # compare the values to one another
    se = s1 == s2
    # if any comparison is False, then not equal
    return all(se)


def dataframes_equals(df1, df2):
    # verify lengths are the same
    if len(df1) != len(df2):
        return False
    # verify each series are equal
    se = [ series_equals(df1[col], df2[col]) for col in df1.columns ]
    print(se)
    return all(se)
        
      
def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == pd.DataFrame:
            return dataframes_equals(expected, received)
        elif type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=0.001)
        else:
            return expected == received
    except Exception as e:
        print(f'EXCEPTION: Raised when checking check_approx_equals {e}')
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    assert check_approx_equals(expected, received), \
        f'Failed: Expected {expected}, but received {received}'