def login():
    
    infileName = input("File with names: ")
    outfileName = input("Destination file: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    
    for i in infile:
        first, last = i.split()
        uname = (first[0]+last[:7]).lower()
        print(uname, file = outfile)
    infile.close()
    outfile.close()
    print("Usernames have been")
    print("written to:", outfileName)
    
