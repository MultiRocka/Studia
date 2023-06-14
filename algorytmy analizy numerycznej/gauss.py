# postępowanie proste
def proste(A, b):
    # sprawdzenie poprawności danych
    if len(A) != len(b):
        raise ValueError("Niepoprawne dane wejściowe: macierz A i wektor b muszą mieć taki sam rozmiar.")
    for row in A:
        if len(row) != len(A):
            raise ValueError("Macierz musi być kwadratowa.")

    n = len(A)


    for k in range(n-1):
        # wybierz element podstawowy
        pivot = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[pivot][k]):
                pivot = i
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            b[k], b[pivot] = b[pivot], b[k]
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
# postępowanie odwrotne
def odwrotne(A, b):
    # sprawdzenie poprawności danych
    if len(A) != len(b):
        raise ValueError("Niepoprawne dane wejściowe: macierz A i wektor b muszą mieć taki sam rozmiar.")
    for row in A:
        if len(row) != len(A):
            raise ValueError("Macierz musi być kwadratowa.")

    n = len(A)
    x = [0] * n


    for k in range(n-1, -1, -1):
        x[k] = b[k]
        for i in range(k+1, n):
            x[k] -= A[k][i] * x[i]
        try:
            x[k] /= A[k][k]
        except ZeroDivisionError:
            raise ValueError("Nie można dzielić przez 0.")
        except ValueError:
            raise ValueError("Nie można pierwiastkować liczby ujemnej.")

    return x

def gauss(A, b):
    proste(A, b)
    return odwrotne(A, b)

# przykładowa macierz A i wektor b
A = [[2, 3, -1], [4, -2, 3], [1, 3, 5]]
b = [5, 12, 8]

x = gauss(A, b)

# wyświetlenie wyniku
print(f"Wektor x: {x}")