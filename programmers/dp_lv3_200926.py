def solution(triangle):
    height = len(triangle)
    NMAX = 500
    dp = [ [ 0 for i in range(NMAX)] for i in range(NMAX)]

    dp[height-1] = triangle[height-1]
    print(dp[height-1])

    for x in range(height-2, -1, -1):
        for y in range(len(triangle[x])):
            dp[x][y] = triangle[x][y] + max(dp[x+1][y], dp[x+1][y+1])
    return dp[0][0]
