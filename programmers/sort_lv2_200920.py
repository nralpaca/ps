import functools

def comp(a,b):
    a_triple = a*3
    b_triple = b*3
    for i in range( min(len(a_triple), len(b_triple)) ):
        if a_triple[i] != b_triple[i]:
            return ord(a_triple[i]) - ord(b_triple[i])
    return len(a) - len(b)

def solution(numbers):
    nstr = list(map(str, numbers))
    ns = sorted(nstr, key=functools.cmp_to_key(comp), reverse=True)
    ans = ''.join(ns)
    if len(ans.strip('0')) == 0:
        return '0'

    return ans