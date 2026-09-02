def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    number_seen = False
    # max 6 characters, min 2
    if len(s) < 2 or len(s) > 6:
        return False
    # splits string to at 2, i.e. 0 and 1 ||| 2, first two characters can't be numbers
    if s[0:2].isalpha() == False:
        return False
    for character in s:
        # rules out punctuation and spaces
        if character in blocked:
            return False
        # if no numbers seen AND character is 0, returns False
        if number_seen == False and character == "0":
            return False
        # if charcter is a number, and previously checked that it isnt the first and isnt 0 if so, changes to number_seen
        if character.isnumeric():
            number_seen = True
        # if character following number is not another number, returns False
        if number_seen == True and character.isalpha():
            return False

    return True

blocked = " ", ".", "!", "?", ":", ";", "'", '"', "-", ",", "(", ")"

main()