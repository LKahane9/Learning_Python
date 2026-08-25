#input a time and output breakfast, lunch, dinner or nothing at all if not the right time

def main():
    usr_inpt = input("what time is it? ").strip()
    convert(usr_inpt)

#removes : converts to int and prints meal time
def convert(time):
    time = int(time.replace(':' , ''))
    if 700 <= time <= 800:
        print("breakfast time")
    elif 1200 <= time <= 1300:
        print("lunch time")
    elif 1800 <= time <= 1900:
        print("dinner time")
    else:
        pass


if __name__ == "__main__":
    main()