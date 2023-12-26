"""Write a function called count_votes that takes a list of numbers 
   indicating votes for candidates 0, 1, or 2 and returns a new list 
   of length 3 showing how many counts each candidate got."""


def count_votes(votes):
    list = [0, 0, 0]
    for i in votes:
        list[i] += 1
    return list
