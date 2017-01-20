# Tree Age

![](http://scienceline.org/wp-content/uploads/2007/03/fir.jpg)

It is well known that the age of a tree can be estimated by some function of the number of rings found within the trunk. **Perfetto Trees** are particularly easy to date, as their age is usually equal to the number of rings. Given a top-down view of a cross section of a Perfetto Tree trunk, determine the age of the tree.

### Input Format

*   An integer `N` denoting the size of the cross section
*   `N` lines, each containing `N` characters which are either `.` or `x`. A `.` represents typical tree innards, whereas an `x` represents a piece of a ring

### Output Format

*   The estimated age of the tree (total number of rings)

Note that rings are defined as connected sequences of `x`'s (connected meaning adjacent in the 4 cardinal directions: up, down, left, or right).

### Sample Input

<pre>
20
....................
....xxxxx...........
....x...x...........
....x...x...........
....xxxxx...........
....................
....................
.xxxxxxxxxxxxxxxxxx.
.x................x.
.x................x.
.x.....xxx........x.
.x.....x.x........x.
.x.....xxx........x.
.x................x.
.xxxxxxxxxxxxxxxxxx.
....................
....................
....................
....................
....................
</pre>



### Sample Output

<pre>
3
</pre>
