# Use open to open file "foo.txt" for reading
filePlaceholder = open("foo.txt")
# Print all the lines in the file
for line in filePlaceholder:
    print(line)
# Close the file
filePlaceholder.close()

# Use open to open file "bar.txt" for writing
fileplaceholder2 = open("bat.txt", 'w')
# Use the write() method to write three lines to the file
fileplaceholder2.write(""" bad music money """)
# Close the file
fileplaceholder2.close()