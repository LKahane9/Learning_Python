# menu provided by cs50
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order()

def order():
    total = 0
    while True:
        try:
            order = input("Item: ").strip().title()
            # adds new item to existing total
            total += menu[order] 
            # rounds to 2 decimals
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            # allows user to exit code with ctrl d or ctrl z i think for windows
            print()
            break

main()