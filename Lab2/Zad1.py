from collections import deque
#from PIL import Image
#im=Image.open('odkurzacz.png')
# Wszystkie możliwe stany 2-polowego świata
stany = [
    ('A', 'brudno', 'brudno'),
    ('B', 'brudno', 'brudno'),
    ('A', 'brudno', 'czysto'),
    ('B', 'brudno', 'czysto'),
    ('A', 'czysto', 'brudno'),
    ('B', 'czysto', 'brudno'),
    ('A', 'czysto', 'czysto'),
    ('B', 'czysto', 'czysto')
]

# Cztery akcje
akcje = ['Lewo', 'Prawo', 'Odkurzaj', 'NicNieRob']

# Sprawdzanie, czy osiągnęliśmy cel (oba pola czyste)
def czy_cel(stan):
    return (stan[1] == 'czysto' and stan[2] == 'czysto')

# Funkcja przejścia: zwraca stan po wykonaniu akcji
def wykonaj_akcje(stan, akcja):
    lokacja, stanA, stanB = stan

    if akcja == 'Lewo' and lokacja == 'B':
        return ('A', stanA, stanB)
    if akcja == 'Prawo' and lokacja == 'A':
        return ('B', stanA, stanB)
    if akcja == 'Odkurzaj':
        if lokacja == 'A':
            return ('A', 'czysto', stanB)
        else:  # lokacja == 'B'
            return ('B', stanA, 'czysto')
    if akcja == 'NicNieRob':
        # Nie zmieniamy stanu
        return stan

    return stan

def bfs(stan_poczatkowy):
    # Jeśli stan początkowy już jest celem, wymuszamy wypisanie ["NicNieRob"]
    # zamiast pustej listy akcji.
    if czy_cel(stan_poczatkowy):
        return [akcje[3]]

    kolejka = deque([(stan_poczatkowy, [])])
    odwiedzone = set([stan_poczatkowy])

    while kolejka:
        stan, sciezka = kolejka.popleft()

        # Sprawdzamy, czy to stan docelowy
        if czy_cel(stan):
            return sciezka

        # Generujemy kolejne stany
        for a in akcje:
            nowy_stan = wykonaj_akcje(stan, a)
            # Jeśli stan jest dozwolony i nie był odwiedzony, dodajemy do kolejki
            if nowy_stan in stany and nowy_stan not in odwiedzone:
                odwiedzone.add(nowy_stan)
                kolejka.append((nowy_stan, sciezka + [a]))

    # W razie braku rozwiązania – choć tu zawsze istnieje – zwracamy pustą listę
    return []

# Sprawdzenie BFS dla wszystkich stanów
if __name__ == "__main__":
    for s in stany:
        wynik = bfs(s)
        print(f"Stan początkowy: {s} -> Akcje: {wynik}")
#im