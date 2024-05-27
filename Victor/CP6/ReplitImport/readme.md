## Reminder
Do the activities in the Instructions and answer these questions. Have a partner 
review your answers and 'sign' his/her name here.

> By signing here I hereby attest that I read the answers and agree that they are full
> and correct. I will gladly accept their grade as my own.   
### Reviwed by: {Student Name}


# Questions:
**Question #1A**   
What is the measured time complexity of your **ORIGINAL** `get_primes` algorithm?
Is it Linear or Quadratic? Does this meet your expectations as you examine 
the code? Explain.  

```
explanation/analysis here. 1-2 sentences
```
**Question #1B**   
What is the measured time complexity of your **Sieve of Eratosthenes** 
implementation of `get_primes`? Does it appear Linear or Quadratic?  
Does this meet your expectations as you examine the code? Explain.  

Feel free to do some online research of Sieve of Eratosthenes.

```
explanation/analysis here. 2-4 sentences
```

**Question #2**   
Examine the `get_sum.png` graph. Explain what the graph is saying about the code 
found in the method `get_sum`. What is the Big-O?
```
explanation here - 1-3 sentences.
```

**Question #3**   
Examine the graphs `limit_range_fast.png` and `limit_range_slow.png`. How do the points 
on each of the graphs grow on the y-axis? Does it look linear? Describe how the 
graphs **look** using Big-O notation.
```
explanation here - 2-4 sentences.
``` 

**Question #4**   
Examine the **code** for the `limit_range_slow`. Explain why it is so slow. 
Explain the Big-O complexity as best you can. Essentially, show the work to 
_derive_ the Big-O complexity. In this example, we will assume that there are n 
values in the list. AND, the range will be of size n. (e.g. n = high - low).   

For reference, the slow code is:
```python
return [ n for n in range(low, high) if n in items]
```

```
explanation/analysis here - 3-5 lines/sentences

``` 

**Question #5**  
Look at the graphs for `get_list_slow`, `get_list_med` and `get_list_fast`. 
Don't forget to look at the scale. What do you suspect is the Big-O complexity 
for each? Explain the speeds of each method.
```
Explanation/analysis here. 3-6 sentences
```