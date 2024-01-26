def is_valid_triangle(a, b, c):
    result = False
    if (((a + b) > c) and ((b + c) > a) and ((c + a) > b)):
        result = True
        return result
    return result

result = is_valid_triangle(7, 5, 10)
print(result)
result = is_valid_triangle(3, 2, 1)
print(result)