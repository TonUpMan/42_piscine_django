import sys

def find_states(states, capital_cities):
    if a in states:
        return (capital_cities[states[a]])
    else:
        return("")

# ##################################################################

def find_capital(states, capital_cities):
    for i in capital_cities:
        if capital_cities[i] == a:
            key = i
    if key:
        for i in states:
            if states[i] == key:
                return(i)
    return("")

# ##################################################################

def create_list(a):
    li = []
    for item in a.split(','):
        li.append(item.strip())
    return li

# ##################################################################

def find_all(a):
    li = create_list(a)
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
    for item in li:
        value = find_capital(states, capital_cities)
        if not value:
            value = find_states(states, capital_cities)
        if not value:
            print(item, "is neither a capital city nor a state")


# ##################################################################

if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_all(a)