def print_numbers():
    with open("numbers.txt") as file:
        data = file.read()
        nbr = ""
        for i in data:
            if i == ',' or i == '\0':
                print(nbr)
                nbr = ""
            else:
                nbr += i
        if nbr:
            print(nbr, end="")

if __name__ == '__main__':
    print_numbers()
