import sys

def find_state(a):
    find = False
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    for i in capital_cities:
        if capital_cities[i] == a:
            key = i
            find = True
    if find:
        for i in states:
            if states[i] == key:
                print(i)
                break
    else:
        print("Unknown capital city")



if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_state(a)