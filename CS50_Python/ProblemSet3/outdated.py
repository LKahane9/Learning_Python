def main():
    yearmd()

def yearmd():
    months = [
        "Blank", # added so that january is 1 and not 0
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June",
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "December"
    ]
    
    while True:
        user_date = input("Date: ").strip()
        # check if input is m/y/d
        if "/" in user_date:
            try:
                month, date, year = user_date.split("/")
                # make sure they fit within the right amount of days and months
                if 0 < int(month) < 13 and 0 < int(date) < 32:
                    # formats to the right amount of decimals
                    print(f"{year:04d}-{int(month):02d}-{int(date):02d}")
                    break
            except ValueError:
                pass
                
        # if written in m d, year format
        # specifically if "," is included!!
        elif "," in user_date:
            try:
                user_date = user_date.replace(",", "")
                month date, year = user_date.split(" ")
                #capitalised so it matched the list of months
                month = month.capitalize()
                if month in months:
                    #if month is in the list, index it to the right number
                    month = months.index(month)
                    if 0 < int(date) < 32:
                        print(f"{year:04d}-{month:02d}-{int(date):02d}")
                        break
            except ValueError:
                pass

main()