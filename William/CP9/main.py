'''
Count how many times each word appears in a file.
Store in a dictionary the true count.
Create a Count-Min Sketch class that will act like
a dictionary, but use much less memory.
Then, do a statistical analysis to see:
1) How many words are perfectly correct
2) The largest error
3) The average error of those that have an error
4) The average error overall
'''

import re
import pandas as pd
from CSE163.William.CP9.to_do.count_min_sketch import CountMinSketch
from CSE163.William.CP9.to_do.web_scrape import get_selector_table
import my_set_client

def read_and_analyze(size):
    '''
    This will read the 'war and peace.txt' and complete a short
    analysis of the counting of the word frequences.
    It will compare the results of a Count-Min Sketch method
    with the actual value calculated with a dictionary.
    '''
    print('using size', size)
    cms = CountMinSketch(size)
    counts = dict()
    max_word = 'a'
    # prime with 'a' word and then fix below
    # this helps reduce if-statements in the loop
    counts[max_word] = 1
    with open('war and peace.txt', 'r') as file:
        for token in file.read().split():
            # remove punctuation
            word = re.sub(r'\W+', '', token.lower())
            # need to remove digits, too
            word = re.sub(r'\d+', '', word)
            if len(word) > 0:
                cms.add(word)
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                if counts[word] > counts[max_word]:
                    max_word = word
    
    counts['a'] -= 1 # correct the initial priming
    print(f'Max Count: dict[{max_word}]={counts[max_word]}')
    print(f'Count of unique words: {len(counts)}')
    print_stats(cms, counts)


def print_stats(cms, counts):
    '''
    cms = the count_min_sketch of all the word counts
    counts = dictionary of true word counts
    '''
    exact = 0
    total_diff = 0
    incorrect = 0
    max_diff = 0
    total = 0
    
    for word in counts.keys():
        cms_val = cms.get(word)
        val = counts[word]
        total += val
        if cms_val != val:
            incorrect += 1
            diff = (cms_val - val)
            if diff > max_diff:
                max_diff = diff
            total_diff += diff
        else:
            exact += 1

    print(f'Exact = {exact}')
    print("Exact% {:.2f}".format(100*exact/len(counts)))
    print(f'incorrect = {incorrect}')
    print("Avg diff = {:.2f}".format(total_diff/incorrect))
    print(f'Max diff = {max_diff}')
    print("Avg count = {:.2f}\n".format(total/len(counts)))

    
def main():
    print(get_selector_table())
    # TODO: Once implemented, run main() in my_set_client
    # my_set_client.main()
    for size in range(200, 901, 100):
        read_and_analyze(size)


if __name__ == '__main__':
    main()
    
    