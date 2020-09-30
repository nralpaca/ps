#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    
    for c in range(len(container)):

        available = sum(container[c]) - container[c][c]
        oth_sum = 0
        for o in range(len(container)):
            if c != o:
                oth_sum += container[o][c]
        print("container{} available {} need to swap{}".format(c, available, oth_sum))


    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
