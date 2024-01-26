vowel = "aeiouAEIOU"

vowel_count = 0
cons_count = 0

string = input()

for i in string:
    if (i >= "A" and i <= "Z") or (i >= "a" and i <= "z"):
        if i in vowel:
            vowel_count += 1
        else:
            cons_count += 1

if (vowel_count > 0 and cons_count > 0) and (vowel_count % 3 == 0 and cons_count % 3):
    print("Aaarr! Me Plunder!!")
else:
    print("Blimey! No Plunder!!")