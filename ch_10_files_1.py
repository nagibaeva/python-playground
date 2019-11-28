# It is essential to learn how to work with files and exeptions.

# Step 1: Read the file into the memory.

# Create the txt file in the same depository as your python files. To open the file from the same directiory use:   with open('name of the file')       the function open() needs only one argument - name of the file. It opens the OBJECT representing the file and assigns it to variable    file_object. 
# The keyword   with    closes the file once accessed as no longer needed.

# Use the read() method to read entire content of the file. We assigned the content of the file the variable    contents. Note: the read() method will print one black line at the end. To remove it you can use: print(contents.rstrip())
# Remember: rstrip() emthod removes any whitespace characters from right side of the string

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
print(contents)

# If your file is stored in another directory, you can specify the direction to the file you want to open. 
# To do so:     with open('direction_to_the_file/file_name.txt')        this method is called RELATIVE FILE PATH

with open('text_files/pi_digits.txt') as new_object:
    new_contents = new_object.read()
print("Next example:")
print(new_contents)

# Or you can do more structured using:      ABSOLUTE FILE PATH and assign variable to it for simplicity.
# file_path = 'full path name as you see in the directory of the file/file_name.txt'
# with open(file_path) as file_object:

file_path = 'D:/Nazgul_python/text_files/pi_digits.txt'
with open(file_path) as file_object:
    third_contents = file_object.read()
    print("One more time")
    print(third_contents)

# Note: You cannot use backslash \ (since it is used to escape character in strings.) If you need to use backslash, use it as double ('c:\\path\\to\\file.txt')

# If you need to examine each line one at a time (or line with specific word in it) use:    for loop:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line) #Here each ln=ine will be printed separately(thus there will be blank space between them)
        #to eliminate blank lines use rstip()
with open(filename) as file_object:
    for line in file_object:        
        print(line.rstrip())
# Note that since we use    with    keyword, the python closes the file automatically and contet of the file is not avaiable outside of with block.
# To acces the content of file outside of the with block, you can store the content (lines) of the file in a list within the with block using   readlines() 
# and then use the list, thant stores the content of file, outside the with block.

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
print("\n")
for line in lines:
    print(line.rstrip())

# WORKING WITH A FILE'S CONTENT:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# Working with large numbers

file_path = 'text_files/pi_million_digits.txt'
with open(file_path) as file_object:
    lines=file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyyyy: ")