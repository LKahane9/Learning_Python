#implement function called convert that turns emoticons into emojis

def main():
    text = input("Input a phrase: ")
    print(convert(text))
#converts both emoticons to the emojis    
def convert(x):
    return x.replace(":)" , "🙂").replace(":(","🙁")

main()