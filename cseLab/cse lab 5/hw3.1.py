def calc_tax(age, salary):
    tax = 0
    if age >= 18:
        if salary >= 10000 and salary <= 20000:
            tax = salary * 0.07
        elif salary > 20000:
            tax = salary * 0.14
    return round(tax)

t = calc_tax(20, 18000)
print(t)