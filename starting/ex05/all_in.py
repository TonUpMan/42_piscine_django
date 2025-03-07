import sys

def find_capital(states, capital_cities, item):
    item = item.lower()
    for i in states:
        if i.lower() == item:
            return(capital_cities[states[i]])
    else:
        return("")

# ##################################################################

def find_states(states, capital_cities, item):
    key = ""
    for i in capital_cities:
        if capital_cities[i].lower() == item.lower():
            key = i
    if key:
        for i in states:
            if states[i].lower() == key.lower():
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
        if item:
            capital = find_capital(states, capital_cities, item)
            state = find_states(states, capital_cities, item)
            if not capital and not state:
                print(item, "is neither a capital city nor a state")
            else:
                if state:
                    print(item.capitalize(), "is the capital of", find_states(states, capital_cities, item))
                else:
                    print(find_capital(states, capital_cities, item),  "is the capital of", item.capitalize())


# ##################################################################

if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = sys.argv[1]
        find_all(a)