'''write a function named switch_pairs() that takes a string argument and
   swaps all adjacent letters (leaving any unpaired letter untouched)'''
   
def switch_pairs(str):
   returnstring = ''
   for i in range(0, len(str), 2):
      returnstring = returnstring + str[i+1] + str[i]
   return returnstring