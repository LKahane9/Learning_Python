#make calculator that calcs tip percentage
#most is provided, just have to remove $ and %, convert the inputed str to float and then fill it out aye


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#converts to float and removes $
def dollars_to_float(d):
    return float(d.replace('$' , ''))

#converrts to float, removes % and divides by 100 so that it is a percent (15 becomes .15)
def percent_to_float(p):
    p = float(p.replace('%' , ''))
    return p / 100

main()