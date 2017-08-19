import json
import difflib

data = json.load(open("./data.json"))

def define(w):
    # make user entry case-insensitive
    w = w.lower()
    if w == 'q':
        exit()
    elif w in data:
        print_formatted_match(w)
    else:
        matches = difflib.get_close_matches(w, data.keys(), n=5)
        for e in matches:
            uc = raw_input("Could not find " + w + " in dictionary. Did you mean " + e + "?" +
                " Enter 'y' for yes or 'n' for no. ")
            if uc.lower() == 'y':
                print("Definition of " + e + ": ")
                print_formatted_match(e)
                return
        print(w + " is not defined in dictionary.")

def print_formatted_match(w):
    i = 1
    for el in data[w]:
        print("(" + str(i) + ") " +el)
        i += 1

while 1:
    w = raw_input("Enter word to look up, or 'q' to exit: ")
    define(w)
