# Ex 4. Glossary2

my_glossary = {
    'phone' : 'a gadget to talk with people on distance', 
    'house' : 'a structure to live in', 
    'book' : 'bunch of paper containg knowledge', 
    'daycare' : 'an organization to look after kids',
    'mom' : 'the best person in the world',
    }

for key, value in my_glossary.items():
    print(f"{key.title()} means {value}")

my_glossary['python'] = 'a number one programming language.'
my_glossary['canada'] = 'a country we live in.'
my_glossary['liam'] = 'my sweet baby boy.'
my_glossary['rem'] = 'my love and my husband.'

print('\n')
for key, value in my_glossary.items():
    print(f"{key.title()} means {value}")

