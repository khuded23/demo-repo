alphanum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}

value = input("enter alphabet:")
print("numerical of {} is {}".format(value, alphanum[value]))
# adding comments to see differences


def addnum(a, b):
    return (a+b)


if __name__ == "__main__":
    addnum
