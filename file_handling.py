fileptr = open("file.txt", "r");

# stores all the data of the file into the variable content
content = fileptr.read(9);

# prints the type of the data stored in the file


# prints the content of the file
print(content)

# closes the opened file
fileptr.close()
