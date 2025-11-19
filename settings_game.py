def fill_pole(pole, size_i, size_j):
    for i in range(size_i):
        pole.append([])
        for j in range(size_j):
            pole[i].append('[_]')


def show_pole(pole, size_i, size_j):
    for i in range(size_i):
        for j in range(size_j):
            print(pole[i],' ', end='')
        print()