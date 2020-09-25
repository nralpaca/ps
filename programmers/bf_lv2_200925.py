def solution(brown, yellow):
    answer = []

    for w in range(1, yellow+1):
        # 24-> 6x4 8x3 12x2 24x1
        h = yellow // w
        if yellow % w != 0: continue
        if h > w: continue
        if w*2 + h*2 + 4 == brown:
            answer.append(w + 2)
            answer.append(h + 2)

    return answer
