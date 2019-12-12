# Cats and Dogs
def read_files(filename):
    """Read the content of file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filename} is not exsisting.")
    else:
        print(f"\n{contents}")

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']
for filename in filenames:
    read_files(filename)