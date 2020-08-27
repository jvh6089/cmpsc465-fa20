# Problem Description

Merge two sorted arrays of integers into a single sorted array.

# Input

Two lines, each line describes a sorted array.  The first number in the line gives
`n`, the number of integers in the array, and the following `n` numbers give
the `n` integers in the array, in ascending order. All numbers are separated by space.

We can assume that 0 <= n <= 100000, and that each number in the arrarys
are in the range of [-2147483648, 2147483647]. 

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C/C++).

# Output

One line, describing the merged sorted array, in ascending order.
The first integer should be the total number of integers in the merged array,
and the following integer should give all numbers in the merged array (in ascending order). 
All numbers should be separated with space.

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C/C++).

# Requirement

Your algorithm should run in linear time, i.e., you are not allowed to call any in-built sort function.

Time limtation: 5 seconds.

Memory limitation: 1.0GB.

# Environment

Your code will be running on Ubuntu 18.04.5.

Now only accept C++ and Python2/Python3 code, g++ version 7.5.0 and Python versions are Python 2.7.17 and Python 3.6.9.

# Examples and Testing

Some examples (e.g., input-x.txt and output-x.txt, x = 1, 2, ...) are provided. 
For Python codes, try the following to test your codes
```
python ./solution.py < input-1.txt > my-output-1.txt
```
For C++ codes, try the following to test your codes
```
g++ -o mybinary solution.cpp
./mybinary < input-1.txt > my-output-1.txt
```

Your output `my-output-1.txt` needs to be *match exactly* to the given `output-1.txt`.
You can use `diff` to compare them:
```
diff my-output-1.txt output-1.txt
```

# Submission

If you want to upload a single file, make sure the file is named as `solution.py` or `solution.cpp`.
If you submit via GitHub, make sure your file is located in directory `assignment1/problem1/solution.py` or `assignment1/problem1/solution.cpp`.


