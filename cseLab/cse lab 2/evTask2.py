totalSec = int(input())

hours = totalSec // 3600
mins = (totalSec - hours * 3600) // 60
sec = totalSec - (hours * 3600 + mins * 60) 

print(f"Hours: {hours}")
print(f"Minutes: {mins}")
print(f"Seconds: {sec}")