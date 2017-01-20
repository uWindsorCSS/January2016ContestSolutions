# Yo-Yo Brah

![](https://pbs.twimg.com/profile_images/652105089205731328/kKuLkqxr.jpg)

<small>Incase this image confuses you, this is a famous Cellist by the name of Yo-Yo Ma</small>

You just bought a new Yo-Yo and are fascinated with how the design changes as it spins. After some careful observation you determine that the Yo-Yo completes exactly one quarter of a clock-wise rotation in approximately 1 millisecond. Given a matrix representing the design of the Yo-Yo before it starts to spin, output the orientation of the design after `N` milliseconds.

### Input Format

*   An integer `N` representing the size of the Yo-Yo
*   `N` lines each containing `N` characters representing the design of the Yo-Yo
*   An integer `M` (>= 0) denoting the number of milliseconds the Yo-Yo will spin for

### Output Format

*   The orientation of the design after the Yo-Yo spins for `M` milliseconds

### Sample Input

<pre>16
       _.-;;-._ 
       '-..-'|   ||   |
       '-..-'|_.-;;-._|
       '-..-'|   ||   |
       '-..-'|_.-''-._|
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       ++++++++++++++++
       2
       </pre>


### Sample Output

<pre>++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
++++++++++++++++
|_.-''-._|'-..-'
|   ||   |'-..-'
|_.-;;-._|'-..-'
|   ||   |'-..-'
 _.-;;-._       
 </pre>

 _Note: Do not worry about the orientation of individual characters (i.e. when you rotate leave ";" as ";")_
