#ask for a file name including .extension, if no suffix or uses another print "application/octet-stream"
def main():
    file_name = input("Input the file name including suffix: ").lower().strip()
    suffix_type(file_name)

#checks n whatnot aye
def suffix_type(file):
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith((".jpeg" , "jpg")):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/ocetet-stream")
          
main()
