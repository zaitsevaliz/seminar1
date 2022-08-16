# Найти расстояние между двумя точками пространства


def quarter(ax, ay, az, bx, by, bz):
    S = bx-ax**2+by-ay**2+(bz-az)**2
    print(S)


quarter(1, 3, 2, 2, 3, 1)
