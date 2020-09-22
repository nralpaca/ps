def solution(phone_book):
    len_list = set()

    for ph in phone_book:
        len_list.add(len(ph))
    len_list = sorted(len_list)

    phone_book = sorted(phone_book, key=lambda x: (len(x), x), reverse=True)
    print(phone_book)

    for l in len_list:
        ld = dict()
        for ph in phone_book:
            if len(ph) >= l:
                if ph[:l] not in ld:
                    ld[ph[:l]] = 1
                elif len(ph) == l:
                    return False
    return True
