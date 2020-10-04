#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    
    for b in range(len(container)):

        for c1 in range(len(container)):  # -= 1            
            if c1 == b:
                continue

            while container[c1][b]:
                target = -1
                for c2 in range(len(container)): # -= 1
                    if c1 == c2 or container[c2][b] == 0:
                        continue
                    
                    target = c2
                    break
                if target == -1:
                    return 'Impossible'
                

        

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
