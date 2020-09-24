
def solution(N, o):
    # 6 0 -> 0 1 [0] 1 0 [1]
    # 6 1 -> 1 0 [1] 0 1 [0]
    if N >= 6:
        print("Love is open door")
    else:
        for i in range(1,N):
            o = (o + 1) % 2
            print(o)
    return 0


N = int(input())
o = int(input())

solution(N, o)