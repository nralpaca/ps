import heapq

def solution(scoville, K):
    answer = 0
    pq = []

    for scov in scoville:
        heapq.heappush(pq, scov)

    while True:
        first = heapq.heappop(pq)
        if first >= K:
            break
        if len(pq) == 0:
            return -1

        second = heapq.heappop(pq)

        scov = first + second * 2
        answer += 1
        heapq.heappush(pq, scov)

    return answer