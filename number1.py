# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def quarter(x, y):
    if x > 0 and y > 0:
        print('1 четверть')
    if x < 0 and y > 0:
        print('2 четверть')
    if x < 0 and y < 0:
        print('3 четверть')
    if x > 0 and y < 0:
        print('4 четверть')


quarter(1, -4)
