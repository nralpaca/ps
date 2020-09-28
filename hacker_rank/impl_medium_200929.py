#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    ans = ''
    dp = [ 1 for i in range(n+1)]
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i
    print(dp[n])


if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)
