hours = int(input())

if hours >= 0 and hours <= 168:
    if hours <= 40:
        print(hours * 200)
    else:
        print(8000 + (hours - 40) * 300)
elif hours < 0:
    print("Hour cannot be negative")
else:
    print("Impossible to work more than 168 hours weekly")