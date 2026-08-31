def main():
    coin = coin_input()
    change(coin)

# input coin, if not 25 10 or 5, return as 0
def coin_input():
        while True:
                coins = int(input("Insert Coin: "))
                if coins == 25 or coins == 10 or coins == 5:
                    return coins
                else:
                    print("Amount Due: 50")

# print amount owed or due
def change(n):
    while True:
        c = int(n)
        if c >= 50:
            print(f"Change Owed: {c-50}")
            break
        elif c < 50:
            print(f"Amount Due: {50-c}")
            n += coin_input()

main()

# improved attempt 2 under coke2.py