def print_numbers():
    with open("numbers.txt") as file:
        data = file.read()
        nbr = data.split(',')
        for item in nbr:
            print(item.strip())

if __name__ == '__main__':
    print_numbers()
