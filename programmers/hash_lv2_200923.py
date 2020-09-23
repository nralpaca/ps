def solution(clothes):
    answer = 1
    cat_dict = dict()

    for c in clothes:
        item, cat = c

        if cat in cat_dict:
            cat_dict[cat].append(item)
        else:
            cat_dict[cat] = [item]

    for key, val in cat_dict.items():
        answer *= (len(val) + 1)
    

    return answer-1
 