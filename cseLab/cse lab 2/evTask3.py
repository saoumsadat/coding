s = float(input())
t = float(input())
velMs = s / t
velKmh = velMs * 3.6
print(velKmh, "km/h")
if velKmh < 60:
    print("Too slow. It needs more changes.")
elif velKmh >= 60 and velKmh <= 90:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")
