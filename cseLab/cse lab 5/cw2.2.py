def is_valid_triangle(a, b, c):
    result = False
    if (((a + b) > c) and ((b + c) > a) and ((c + a) > b)):
        result = True
        return result
    return result

def tri_area(a, b, c):
    if is_valid_triangle(a, b, c):
        s = (a + b + c) / 2
        area = ((s * (s - a) * (s - b) * (s - c))) ** 0.5
        print(round(area, 3))
    else:
        print("Can't form triangle")

tri_area(3, 2, 1)
tri_area(7, 5, 10)