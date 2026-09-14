def main():
  # prints what is returned by the function aye
    shopping = shop()
    # splits each key into the str key and the str value, n then prints aye
    for key, value in shopping.items():
        print(f"{value} {key}")

def shop():
    # makes a dict for this function
    shopping_list = {}
    while True: 
        try:
            item = input("").upper().strip()
        except EOFError:
            # if ctrl d inputed, sort the dict by keys (alphabetically)
            shopping_list = dict(sorted(shopping_list.items()))
            print()
            return(shopping_list)
        else:
            # if in the dict, val + 1, else the key and value are created
            if item in shopping_list:
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1
main()