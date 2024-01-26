pi = 3.141592653589793

def circle(r):
    area = pi * (r ** 2)
    return area

def sphere(r):
    volume = (4/3) * pi * (r**3)
    return volume

def fitting(d1, d2, dim):
    r1 = d1 / 2
    r2 = d2 / 2
    rem_area = 0
    if dim == 2:
        area1 = circle(r1)
        area2 = circle(r2)
        if area1 > area2:
            rem_area = area1 - area2
            print(f"Circle-2 can fit inside Circle-1 and {round(rem_area, 3)} square units would be left.")
        elif area1 < area2:
            rem_area = area2 - area1
            print(f"Circle-1 can fit inside Circle-2 and {round(rem_area, 3)} square units would be left.")
        else:
            print("Impossible to fit.")

    elif dim == 3:
        vol1 = sphere(r1)
        vol2 = sphere(r2)
        if vol1 > vol2:
            rem_vol = vol1 - vol2
            print(f"Sphere-2 can fit inside Sphere-1 and {round(rem_vol, 3)} cubic units would be left.")
        elif vol1 < vol2:
            rem_vol = vol2 - vol1
            print(f"Sphere-1 can fit inside Sphere-2 and {round(rem_vol, 3)} cubic units would be left.")
        else:
            print("Impossible to fit.")
fitting(8, 10, 2)
fitting(30, 14, 3)
fitting(5, 5, 3)