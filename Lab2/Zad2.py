import numpy as np
from queue import PriorityQueue

# Stan docelowy, który chcemy osiągnąć w układance
cel = np.array([[1,2,3],
                [4,5,6],
                [7,8,0]])

# Funkcja obliczająca heurystykę (sumę odległości Manhattan)
def heurystyka(stan, cel):
    suma = 0
    # Liczymy dystans każdej liczby od jej docelowego miejsca
    for liczba in range(1,9):
        x_stan, y_stan = np.where(stan == liczba)
        x_cel, y_cel = np.where(cel == liczba)
        suma += abs(x_stan[0] - x_cel[0]) + abs(y_stan[0] - y_cel[0])
    return int(suma)

# Funkcja, która sprawdza, czy dany stan jest już stanem docelowym
def czy_cel(stan):
    return np.array_equal(stan, cel)

# Funkcja, która znajduje wszystkie możliwe ruchy pustego pola (oznaczonego jako 0)
def znajdz_ruchy(stan):
    ruchy = []
    x, y = np.where(stan == 0)  # znajdź pozycję pustego pola (0)
    x, y = x[0], y[0]

    # Możliwe kierunki ruchu: góra, dół, lewo, prawo
    kierunki = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

    for nowy_x, nowy_y in kierunki:
        # Sprawdź czy nowa pozycja jest w granicach planszy
        if 0 <= nowy_x < 3 and 0 <= nowy_y < 3:
            nowy_stan = stan.copy()
            # Zamieniamy miejscami 0 z sąsiadującą liczbą, tworząc nowy stan
            nowy_stan[x,y], nowy_stan[nowy_x,nowy_y] = nowy_stan[nowy_x,nowy_y], nowy_stan[x,y]
            ruchy.append(nowy_stan)

    return ruchy

# Algorytm przeszukiwania A*
def a_star(start):
    # Kolejka priorytetowa przechowująca stany do sprawdzenia, zaczynamy od stanu początkowego
    kolejka = PriorityQueue()
    # Wstawiamy pierwszy stan: (koszt, stan, ścieżka ruchów)
    kolejka.put((0, start.tolist(), []))

    # Zbiór odwiedzonych stanów, aby nie sprawdzać ich ponownie
    odwiedzone = set()

    # Dopóki kolejka nie jest pusta, kontynuujemy poszukiwania
    while not kolejka.empty():
        # Pobieramy stan z najmniejszym kosztem całkowitym (heurystyka + wykonane kroki)
        koszt, stan, sciezka = kolejka.get()
        stan_np = np.array(stan)

        # Sprawdź czy aktualny stan jest stanem docelowym
        if czy_cel(stan_np):
            # Jeśli tak, drukujemy całą sekwencję ruchów
            print("Znaleziono rozwiązanie! Sekwencja kroków:")
            for krok in sciezka:
                print(np.array(krok))
                print("-----")
            print(stan_np)
            print("Dotarliśmy do celu!")
            print(f"Ilość kroków: {len(sciezka)}")
            return

        # Zapisujemy obecny stan jako odwiedzony
        odwiedzone.add(str(stan_np))

        # Dla każdego możliwego kolejnego ruchu
        for ruch in znajdz_ruchy(stan_np):
            # Jeżeli stan po wykonaniu ruchu nie był wcześniej odwiedzony
            if str(ruch) not in odwiedzone:
                # Tworzymy nową ścieżkę zawierającą obecny stan
                nowa_sciezka = sciezka + [stan]
                # Koszt g(n) - liczba kroków wykonanych do tej pory
                g = len(nowa_sciezka)
                # Heurystyka h(n) - przewidywana liczba kroków do celu
                h = heurystyka(ruch, cel)
                # Całkowity koszt f(n) = g(n) + h(n)
                f = g + h
                # Dodajemy nowy stan do kolejki priorytetowej
                kolejka.put((f, ruch.tolist(), nowa_sciezka))

# Definiujemy stan początkowy zgodny z zadaniem
start = np.array([[0,1,3],
                  [4,2,5],
                  [7,8,6]])

# Uruchamiamy algorytm A* od stanu początkowego
a_star(start)