import sys

def find_capital(a):
    key = ""
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
    if key:
        for i in states:
            if states[i] == key:
                print(i)
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_capital(a)