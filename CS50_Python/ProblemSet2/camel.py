# change inputed text from being formatted in camel case (theTallLad) into snake case (the_tall_lad)
# assume the inputted text will be in camel case

def main():
    camel_case = input("camelCase: ").strip()
    #convert to list to seperate all characters of the string
    camel_char = list(camel_case)
    convert(camel_char)

def convert(n):
    #if character is upper, lowers it and prints with a _ beforehand, and then repeats with next value in n
    for character in n:
        if character.isupper():
            print(f"_{character.lower()}", sep='', end='')
        else:
            print(character, sep='', end='')
    # print() at the end so that a new line is at the end, otherwise it prints and on the same line it prints my hostname:username and path
    print()
        
main()