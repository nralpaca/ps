from queue import PriorityQueue

def solution(scoville, K):
    answer = 0

    pq = PriorityQueue()

    for scov in scoville:
        pq.put(scov)

    while True:
        first = pq.get()
        if first >= K:
            break

        second = pq.get()

        scov = first + second * 2
        answer += 1
        pq.put(scov) 

    return answer
