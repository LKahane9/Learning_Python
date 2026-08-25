#ask person to input the math required, calculates and outputs as a float to one decimal
#format as x y z, x is an int, y is either + - / or *, z is another int
def main():
    x, y, z = input("What equation do you want solved? ").strip().split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        answer = float(x + z)
        print(round(answer , 1))
    elif y == "-":
        answer = float(x - z)
        print(round(answer , 1))
    elif y == "/":
        if z != 0:
            answer = float(x / z)
            print(round(answer , 1))
        else:
            print("You can't divide by zero.")
    elif y == "*":
        answer = float(x * z)
        print(round(answer , 1))
    else:
        print("try a new operator (* + - /)")

main()