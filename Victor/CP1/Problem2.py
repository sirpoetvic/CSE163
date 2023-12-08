# filter_long_lines

'''Write a method called filter_long_lines that takes a file name
and a minimum number of words and prints out all of the lines
in the file with at least that many words (tokens separated by spaces).'''

def filter_long_lines(filename, minnum):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            if(len(tokens) >= minnum):
                print(line)