def main():
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    dollars = dollars_to_float(dollars)
    percent = percent_to_float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d
def percent_to_float(p):
    p = float(p.replace("%", ""))
    p = p/100
    return p

main()
