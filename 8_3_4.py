# Ex 8_3 T-Shirt

def make_shirt(size, picture):
    """Display information about t-shirt"""
    print(f"\nPrinting t-shirt size {size} and with print '{picture.title()}'.")
make_shirt('8','freedom')
make_shirt(picture = 'peace', size = '6')

def make_shirt_1(picture = 'i love python', size = 'large'):
    """Display information about t-shirt"""
    print(f"\nPrinting t-shirt size {size} and with print '{picture.title()}'.")
make_shirt_1(picture = 'in da house')
make_shirt_1(size = 'medium')
make_shirt_1(picture = 'made in ussr', size = 'small')