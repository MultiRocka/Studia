import cmath

def householder(a):

    v = list(a)

    # Obliczenie skalara
    alpha = sum(x ** 2 for x in v)
    if alpha == 0:
        raise ValueError("Wektor a nie może być wektorem zerowym.")
    v[0] += cmath.sqrt(alpha) if v[0] < 0 else -cmath.sqrt(alpha)

    # Obliczenie macierzy P
    P = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            P[i][j] = -2 * v[i] * v[j] / sum(x ** 2 for x in v)
    P[0][0] += 1

    return P

a = [1, 2, 3]
P = householder(a)
for row in P:
    print(row)
