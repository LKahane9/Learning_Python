#get user input and removes whitespace from left and right AND replaces spaces with '...'
text = input("Input your text to be 'slowed' down: ").strip().replace(" ", "...")

print(text)