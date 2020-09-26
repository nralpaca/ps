

def solution(triangle):
    answer = 0
    height = len(triangle)
    NMAX = 500
    dp = [ [ 0 for i in range(NMAX)] for i in range(NMAX)]

    dp[height-1] = triangle[height-1]
    print(dp[height-1])

    for x in range(height-2, -1, -1):
        for y in range(len(triangle[x])):
            dp[x][y] = triangle[x][y] + max(dp[x+1][y], dp[x+1][y+1])

    print(dp[0][0])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))