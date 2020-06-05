"""Программа по поиску кратеров на луне."""


def calculate(matrix: list) -> int:
    """Функция вычисления кратеров."""
    n = len(matrix)
    m = len(matrix[0])
    b: list = [[]]
    t = 0
    count = 0

    for i in range(0, n + 2):
        if t != i:
            b.append([])
            t = i
        for j in range(0, m + 2):
            b[i].append(0)
    print(b)

    def exclude(i: int, j: int) -> None:
        if b[i][j] != 1:
            return
        b[i][j] = 0
        exclude(i + 1, j)
        exclude(i - 1, j)
        exclude(i, j + 1)
        exclude(i, j - 1)

    for i in range(1, len(data) + 1):
        for j in range(1, len(data[0]) + 1):
            b[i][j] = data[i - 1][j - 1]

    for i in range(1, len(data) + 1):
        for j in range(1, len(data) + 1):
            if b[i][j] == 1:
                count += 1
                exclude(i, j)
    return count


data = []
with open('Craters.txt') as file_with_craters:
    for line in file_with_craters:
        data.append([int(x) for x in line.split()])

print(calculate(data))

