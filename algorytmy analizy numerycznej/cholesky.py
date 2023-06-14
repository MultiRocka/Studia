import cmath

def cholesky(A):
    n = len(A)

    if n == 0:
        raise ValueError("Macierz nie może być pusta")

    # Sprawdzenie, czy macierz jest kwadratowa
    if not all(len(row) == n for row in A):
        raise ValueError("Macierz musi być kwadratowa")

    # Sprawdzenie, czy macierz jest symetryczna
    if not all(A[i][j] == A[j][i] for i in range(n) for j in range(n)):
        raise ValueError("Macierz musi być symetryczna")

    # Sprawdzenie, czy macierz jest dodatnio określona
    if not all(A[i][i] > 0 for i in range(n)):
        raise ValueError("Macierz musi być dodatnio określona")

    # Inicjalizacja macierzy L
    L = [[0] * n for _ in range(n)]

    # Algorytm rozkładu Choleskiego
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                L[i][j] = cmath.sqrt(A[i][i] - s)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]

    return L

A = [[4, -1j, 1+1j],
     [-1j, 5, -1-2j],
     [1+1j, -1-2j, 6]]
L = cholesky(A)
if L is None:
    print("Macierz nie spełnia warunków rozkładu Choleskiego.")
else:
    for row in L:
        print(row)