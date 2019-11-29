with open('text_files/learning_python.txt') as file_object:
    content = file_object.read()
print(content.strip())

print("\n")
with open('text_files/learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())

print("\n")
with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    message = line.strip()
    print(message.replace('Python', 'C'))