# Ex 8_7 Albums

def make_album(name, title, number = None):
    """Return a dictionary with information about album"""
    full = {'artist name' : name, 'album title' : title}
    if number:
        full['number of songs'] = number
    return full
album = make_album('drake', 'world is mine')
print(album)

album = make_album('zara', 'winter magic', 18)
print(album)

album = make_album(name = 'lil one', number = 23, title = 'crazy')
print(album)