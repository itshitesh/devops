with open("absolute path of file ", "r") as o:

    content = o.read()
    words = len(content.split())
    print("There are " + str(words) + " words in the file.")

