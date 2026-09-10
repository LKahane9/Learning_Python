def main():
    calc()

def calc():
     # inf loop to keep asking for input if invalid or error
    while True:
        try:
            x,y = input("Fraction: ").strip().split('/')
            x, y = map(int, (x, y))
           # value Error if x smaller than 0 or bigger than y
            if x < 0 or x > y:
                raise ValueError
            percent_fuel = round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if percent_fuel <= 1:
                print("E")
                break
            elif percent_fuel >= 99:
                print("F")
                break
            else:
                print(f"{percent_fuel}%")
                break

main()