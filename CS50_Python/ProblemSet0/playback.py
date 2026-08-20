#get user input and removes whitespace from left and right
text = input("Input your text to be 'slowed' down: ").strip()
#replace spaces with "..."
text = text.replace(" ", "...")
print(text)