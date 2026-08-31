# list including vowels
replace = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ").strip()
    print("Output: ", end='')
    vowels(text)

def vowels(x):
    for character in x:
        # prints character unless in replace (list including vowels)
        # converts character to lowercase to check against list, will still print character as uppercase if thats how its formatted tho
        # only converts to check against the list
        if character.lower() not in replace:
            print(character, end='')
    print()

main()