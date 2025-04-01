def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_no_dollar = d.replace('$','')
    return float(d_no_dollar)


def percent_to_float(p):
    p_no_perc = p.replace('%','')
    return 1/100*float(p_no_perc)


main()
