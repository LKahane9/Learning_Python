#if greeting start with hello output $0, if starts with an h but isnt hello, $20 otherwise $100, ignore whitespace and casing

greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
    