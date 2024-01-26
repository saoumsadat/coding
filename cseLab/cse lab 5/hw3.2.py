def calc_tax(age, salary):
    tax = 0
    if age >= 18:
        if salary >= 10000 and salary <= 20000:
            tax = salary * 0.07
        elif salary > 20000:
            tax = salary * 0.14
    return round(tax)

def calc_yearly_tax():
    age = int(input())
    total_tax = 0
    for x in range(1, 13):
        monthly_salary = int(input())
        tax = float(calc_tax(age, monthly_salary))
        if not(tax):
            tax = int(tax)
        total_tax += tax
        print(f"Month{x} tax: {tax}")
    print(f"Total Yearly Tax: {total_tax}")

calc_yearly_tax()