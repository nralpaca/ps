
def solution(priorities, location):
    answer = 1
    docs = []
    for i in range(len(priorities)):
        if i == location:
            docs.append([priorities[i],True]) 
        else:
            docs.append([priorities[i],False])

    while len(docs) != 0:
        mmax = max([x[0] for x in docs])
        doc = docs.pop(0)
        if doc[0] < mmax:
            docs.append(doc)
        elif doc[1] == True:
            break
        else:
            answer += 1

    return answer