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
    data = a.split()
    for i in data:
        print(i)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_state(a)