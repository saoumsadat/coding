def nested_to_linear(a):
    l = []
    for x in a:
        if type(x) != list:
            l.append(x)
        else:
            l = l + nested_to_linear(x)
    return l


a = ["start", 10, [4, 2, [11, [9, "mid", 3, [1, 0], 6]], 8], "Done"]

print(nested_to_linear(a))