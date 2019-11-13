# Return value of functions:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Note: you need a variable that return value will be assigned to.

# In order to make optional parameter, that is not required but can be added:   use defalut value of empty string ""

def get_formatted_name_1(first_name, last_name, middle_name = ""):
    """Return full and formated name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name_1('jimi', 'hendrexon')
print(musician)

musician = get_formatted_name_1('john', 'hooker', 'lee')
print(musician)

# Return value can take more complicated forms as of lists and dictionaries:

def build_person(first_name, last_name):
    """Return a dictionary of information about person"""
    person = {'first' : first_name, 'last' : last_name}
    return person
musician = build_person('john', 'legend')
print(musician)


# Note: you can add any optional parameter by setting default value to empty string or None:

def build_person_1(first_name, last_name, age = None):
    """Return a dictionary of information about person"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person
musician = build_person_1('david', 'guetta')
print(musician)

musician = build_person_1('ezra', 'miller', age = 27)
print(musician)

