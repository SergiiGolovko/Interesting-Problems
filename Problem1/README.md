## Find the smallest positive integer missing in array.

### Problem Statement.

Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

For another example, given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

### Problem Solution. 

Python script ```solution.py``` contains code solution. It solves the problem with time complexity O(N) and space complexity O(1),
beyond input storage.

### Why it works?

  * After the first loop, on the `i`-th place of list ```l``` either ```i + 1``` of `i` is not in the array `l`. We count from zero to
  be consistent with python.
    
   *Proof*: we go over entire array and put ```a``` on ```a - 1``` place if it is between `1` and `N`.
   
  * Function returns the smallest positive integer missing in the array.
  
   *Proof*: kind of obvious after the first statement is proved.
  
  * Space complexity is O(1).
  
   *Proof*: we use only two additional variables `a` and `n`.
   
  * Time complexity is O(n).
  
   *Proof*: the hardest part. It sufficient to show that the body of `while` loop executed O(N) times. For each number `a` in the array
   let `k_a` defines number of times `a` appeared in the array. If `a <= 0` or `a > N` then body of `while` loop executed `0` times. If
   `a > 0` and `a <= N`, if `a` appears on `a - 1` position then body of `while` loop executed `0` times for this position; and if `a` apears on other position then body of
   while loop executed exactly one time for that position and `a` as after that another number appears at that position. So, in total for
   each `a` body of `while` loop executed no more than $k_a$ times. In total body of `while` loop executed no more than `sum k_a <= N`. We
   also proved that program will eventually terminate.

### Tests. 

Python script ```tests.py``` contains few tests. To run tests simply run ```python tests.py```.

