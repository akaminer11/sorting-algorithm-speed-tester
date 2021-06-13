# sorting-algorithm-speed-tester
A compilation of my implementations of the 5 most popular sorting algorithms. Has a main program to smoothly test times and such.

Used in the command line. No GUI to speak of. Sorry.

## Download Information
You need to have everything downloaded and in the same folder in order for the main program to work.

If you only want to run a single algorithm, they each have a main program so you can run them on their own. You will, however, need to have the gen_random utility program.
If you want to duplicate it, it is like 5 lines of code.

## Notes
Everything except quicksort returns a new list without actually changing the original. That was just due to me being stupid.

These may not be the absolutely fastest implementations of the algorithms, but they basically follow the standard steps for the algorithm.

This is written in python3. It may not be unbelievably speedy.

Recursion limits on quicksort and mergesort may prevent very big lists from being sorted. You can set the recursion limit to a higher number relatively easily by just messing in the source code.
