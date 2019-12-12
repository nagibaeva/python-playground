# Common words

def count_common_words(filename):
    """COunt the common word in the file."""
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
        common_words = contents.count('Alice')
        print(common_words)
filename = 'text_files/alice.txt'
count_common_words(filename)