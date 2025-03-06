import sys

def find_state(a):
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
    if a in states:
        print(capital_cities[states[a]])
    else:
        print("Unknown state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_state(a)