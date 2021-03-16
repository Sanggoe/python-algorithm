### Simple Array Sum

Given an array of integers, find the sum of its elements.

For example, if the array ar = [1,2,3], 1+2+3=6, so return 6.

<br/>

#### Function Description

Complete the *simpleArraySum* function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

- *ar*: an array of integers

<br/>

#### **Input Format**

The first line contains an integer, n, denoting the size of the array.
The second line contains space-separated integers representing the array's elements.

<br/>

#### **Constraints**

0 < n, ar[i] <= 1000

<br/>

#### **Output Format**

Print the sum of the array's elements as a single integer.

<br/>

#### **Sample Input**

```
6
1 2 3 4 10 11
```

<br/>

#### **Sample Output**

```
31
```

<br/>

#### **Explanation**

We print the sum of the array's elements: 1+2+3+4+10+11=31.

<br/>

#### Source Code

```python
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum = 0
    for n in ar:
        sum+=n    
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
```
