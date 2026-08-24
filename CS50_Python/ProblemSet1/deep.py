#implement program that prompts for an answer, outputs yes if the answer 42 forty two or forty-two, otherwise no

meaning = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if meaning == "42" or meaning == "forty-two" or meaning == "forty two":
    print("Yes")
else:
    print("No")