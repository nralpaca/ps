#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ans = []
    rset = set()
    for r in ranked:
        rset.add(-r)
    s_ranked = sorted(rset)
    print(s_ranked)

    for p in player:
        a = bisect.bisect_right(s_ranked, -p)
        if s_ranked[a-1] == -p:
            ans.append(a)
        else:
            ans.append(a+1)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

'''
6
100 90 90 80 75 60
5
50 65 77 90 102

'''
