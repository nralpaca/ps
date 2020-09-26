def solution(m, n, puddles):

    dp = [ [0 for _ in range(m+1)] for _ in range(n+1) ]
    dp[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] not in puddles:
                if x-1 == 1 and y ==1 or x == 1 and y-1 == 1:
                    dp[x][y] = 1
                else:
                    dp[x][y] = (dp[x-1][y] + dp[x][y-1]) % 1000000007


    return dp[n][m]