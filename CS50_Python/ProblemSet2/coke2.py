# second attempt with help from google / youtube
# have to remember to use caps for amount due change owed etc. or will fail check50
# 'assume that user will input integers' - dont need to conv from str to int with .isdigit()

def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        # checks list to see if coin is valid, if it is 
        if coin in [25, 10, 5]:
            amount_due = amount_due - coin
    #converts neg to positive, otherwise would output something like -25
    amount_due = abs(amount_due)
    print(f"Change Owed: {amount_due}")

main()

# i think this should work properly