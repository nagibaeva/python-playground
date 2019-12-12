def count_words(filename):
    """Count approximate amount of words in files."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass # It will make the program fail without reporting the fail.
        # print(f"Sorry, the file {filename} does not exist.") 
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"\nThe file {filename} has about {num_words} words.")

filename = 'text_files/alice.txt'
count_words(filename)

filenames = [
    'text_files/alice.txt', 
    'text_files/siddhartha.txt', 
    'text_files/moby_dick.txt', 
    'text_files/little_women.txt',
    ]
for filename in filenames:
    count_words(filename)