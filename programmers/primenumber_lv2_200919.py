from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    sset = set()

    for n in range(1, len(numbers)+1):
        perm = permutations(list(numbers), n)

        for p in perm:
            num = int(''.join(p))
            if is_prime(num) == True:
                sset.add(num)
    return len(sset)