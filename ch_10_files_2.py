# Writing to the files.
# Python can write to txt documents. To do so, use: open(name_of_file, 'w')     where w tells python to open the file in witing mode.
# more modes: 'r' - read mode, 'w' - write mode, 'a' - append mode, 'r+' - read and write mode

filename = 'text_files/programming_1.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming, but now not very good at it.\n") # Add \n to make each sentence on own line
    file_object.write("I study python every day.\n")

with open(filename, 'a') as file_object:
    file_object.write("I am currently on chapter 10.\n")
    file_object.write("Soon, I will finish the basics of python and start doing project of the book.\n")