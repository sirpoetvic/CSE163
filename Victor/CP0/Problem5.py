'''Write a function named find_range() that takes a list of integers
   and returns the range of values found in the list.'''
   
def find_range( list ):
   if(max(list) == min(list)):
      return 1
   else:
      return max(list) - min(list)