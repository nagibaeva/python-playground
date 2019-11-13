# Ex 8_9 User Album

def make_album(name, title, number):
    """Return a full formated dictionary of album"""
    full_name = {'artist name' : name, 'title of album': title, 'number of songs' : number}
    return full_name

while True:
    print("\nTell me about your favorite artist and album.")
    print("Enter 'q' any time if you want to quit.\n")
        
    name = input("Enter the name of artist: ")
    if name == 'q':
        print("\nGood bye!")
        break
    title = input("Enter the name of album: ")
    if title == 'q':
        print("\nGood bye!")
        break
    number = input("Enter the number of songs in the album: ")
    if number == 'q':
        print("\nGood bye!")
        break
        
    album = make_album(name, title, number)
    print(album)