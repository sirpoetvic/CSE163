## Reminder
Do the activities in the Instructions and answer these questions. Have a partner 
review your answers and 'sign' his/her name here.

> By signing here I hereby attest that I read the answers and agree that they are full
> and correct. I will gladly accept their grade as my own.   
### Reviwed by: Ian Kraemer


# Questions:
**Question #1A**   
What is the measured time complexity of your **ORIGINAL** `get_primes` algorithm?
Is it Linear or Quadratic? Does this meet your expectations as you examine 
the code? Explain.  

```
I think it is linear because there appears to be no curve that resembles a quadratic - it is mostly a straight line. It meets my expectations I believe. 
I would assume, it is not the most efficent, since I am copying an entire set and removing input values, but it also isn't the slowest since I am using
the sqrt(n) and i*i which reduce redundancy. 
```
**Question #1B**   
What is the measured time complexity of your **Sieve of Eratosthenes** 
implementation of `get_primes`? Does it appear Linear or Quadratic?  
Does this meet your expectations as you examine the code? Explain.  

Feel free to do some online research of Sieve of Eratosthenes.

```
I believe I did the "Sieve of Eratosthenes" algorithim in my solution. This was my "original," so my answers and thoughts stay the same. Not the slowest, but 
probably not the fastest way?
```

**Question #2**   
Examine the `get_sum.png` graph. Explain what the graph is saying about the code 
found in the method `get_sum`. What is the Big-O?
```
The code in get_sum follows an O(n^2), since it follows the quadratic loop. This means that it isn't the most efficient. It makes sense that it is O(n^2) since
the code has nested for loops; O(n) for the first loop, and for each of those, it is iterating another O(n), which is n^2. 
```

**Question #3**   
Examine the graphs `limit_range_fast.png` and `limit_range_slow.png`. How do the points 
on each of the graphs grow on the y-axis? Does it look linear? Describe how the 
graphs **look** using Big-O notation.
```
On limit_range_fast, it looks almost linear. I can tell it is a little bit quadratic becasue it has a slight curve up, but other than that it looks linear.
On limit_range_slow, it is for sure a steeper quadratic. Doesn't really look linear.
As such, this would mean that limit_range_fast has an O(n), and limit_range_slow has an O(N^2)
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
So this is a condensed loop. Iterating through low and high once is O(n). Since the "if n in items" checks of n is present in items (iterating through it, instead of checking for a condition), that is also O(n). Since it is a nested loop, just condensed, that would mean that the complexity will be O(n^2) because it is iterating through something twice, instead of once and checking for a condition. 

``` 

**Question #5**  
Look at the graphs for `get_list_slow`, `get_list_med` and `get_list_fast`. 
Don't forget to look at the scale. What do you suspect is the Big-O complexity 
for each? Explain the speeds of each method.
```
get_list_slow has an o(n^2), because it follows a quadratic. 
get_list_med looks like o(n), since the graph appears linear and the y axis scale is significantly less than the previous.
get_list_fast looks also like o(n), since it is also mostly linear and the y axis scale is significantly less than the previous.

Looking at the code for each, it appears that the premise is still the same - just the loop range conditions and methods are affecting the time complexity. 

For get_list_slow, the insert is shifting everything over one, which I think adds to the slowness of the algorithim. get_list_med puts the value to the end of the list, which is much more efficient than pushing everything over, then inserting a value in the list. get_list_fast is the fastest, mainly beacuse it removes the usage of the methods .insert and .append, and directly creates the list using the [].
```