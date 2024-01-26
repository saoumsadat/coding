def one_to_N(curr, last):
    print(curr, end=" ")
    if curr == last:
        return
    one_to_N(curr + 1, last)

one_to_N(1, 5)

