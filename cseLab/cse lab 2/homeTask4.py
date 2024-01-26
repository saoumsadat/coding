hour = int(input())
msg = ''

if hour >= 4 and hour <= 6:
    msg = "Breakfast"
elif hour >= 12 and hour <= 13:
    msg = "Lunch"
elif hour >= 16 and hour <= 17:
    msg = "Snacks"
elif hour >= 19 and hour <= 20:
    msg = "Dinner"
elif hour >= 0 and hour <= 23:
    msg = "Patience is a virtue"
else:
    msg = "Wrong time"

print(msg)