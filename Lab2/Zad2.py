# Prosta gra układanka 8-puzzle z algorytmem A*

# Cel jaki chcemy osiągnąć
CEL = "12345678 "


# Funkcja do pokazywania układanki
def pokaz_ukladanke(stan):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(f" {stan[i * 3 + j]} |", end="")
        print("\n-------------")
    print()


# Obliczanie odległości Manhattan między klockami
def oblicz_odleglosc(stan):
    suma = 0
    for pozycja in range(9):
        klocek = stan[pozycja]
        if klocek == ' ':
            continue

        # Gdzie powinien być klocek
        docelowa_pozycja = int(klocek) - 1

        # Obecne współrzędne
        obecny_wiersz = pozycja // 3
        obecna_kolumna = pozycja % 3

        # Docelowe współrzędne
        docelowy_wiersz = docelowa_pozycja // 3
        docelowa_kolumna = docelowa_pozycja % 3

        suma += abs(obecny_wiersz - docelowy_wiersz) + abs(obecna_kolumna - docelowa_kolumna)
    return suma


# Znajdź możliwe ruchy
def znajdz_ruchy(stan):
    puste = stan.index(' ')
    wiersz = puste // 3
    kolumna = puste % 3
    ruchy = []

    # Sprawdź wszystkie kierunki
    # W górę
    if wiersz > 0:
        nowa_pozycja = (wiersz - 1) * 3 + kolumna
        nowy_stan = list(stan)
        nowy_stan[puste], nowy_stan[nowa_pozycja] = nowy_stan[nowa_pozycja], nowy_stan[puste]
        ruchy.append((''.join(nowy_stan), 'Góra'))

    # W dół
    if wiersz < 2:
        nowa_pozycja = (wiersz + 1) * 3 + kolumna
        nowy_stan = list(stan)
        nowy_stan[puste], nowy_stan[nowa_pozycja] = nowy_stan[nowa_pozycja], nowy_stan[puste]
        ruchy.append((''.join(nowy_stan), 'Dół'))

    # W lewo
    if kolumna > 0:
        nowa_pozycja = wiersz * 3 + (kolumna - 1)
        nowy_stan = list(stan)
        nowy_stan[puste], nowy_stan[nowa_pozycja] = nowy_stan[nowa_pozycja], nowy_stan[puste]
        ruchy.append((''.join(nowy_stan), 'Lewo'))

    # W prawo
    if kolumna < 2:
        nowa_pozycja = wiersz * 3 + (kolumna + 1)
        nowy_stan = list(stan)
        nowy_stan[puste], nowy_stan[nowa_pozycja] = nowy_stan[nowa_pozycja], nowy_stan[puste]
        ruchy.append((''.join(nowy_stan), 'Prawo'))

    return ruchy


# Główny algorytm A*
def szukaj_rozwiazania(start):
    kolejka = [(start, [], 0)]  # (stan, historia ruchów, koszt)
    odwiedzone = set()
    krok = 0

    while kolejka:
        # Sortuj kolejke według kosztu + heurystyki
        kolejka.sort(key=lambda x: x[2] + oblicz_odleglosc(x[0]))
        bierzacy_stan, historia, koszt = kolejka.pop(0)

        krok += 1
        h = oblicz_odleglosc(bierzacy_stan)
        f = koszt + h
        print(f"\n=== Krok {krok} ===")
        print(f"Stan: g(n) = {koszt}, h(n) = {h}, f(n) = {f}")
        pokaz_ukladanke(bierzacy_stan)

        if bierzacy_stan == CEL:
            print("!!! ZNALEZIONO ROZWIĄZANIE !!!")
            print("Kolejność ruchów:")
            for i, ruch in enumerate(historia):
                print(f"{i + 1}. {ruch}")
            return historia

        odwiedzone.add(bierzacy_stan)

        # Sprawdź możliwe ruchy
        for nowy_stan, ruch in znajdz_ruchy(bierzacy_stan):
            if nowy_stan not in odwiedzone:
                g = koszt + 1
                h = oblicz_odleglosc(nowy_stan)
                f = g + h
                print(f"  Możliwy ruch: {ruch} — g(n) = {g}, h(n) = {h}, f(n) = {f}")
                pokaz_ukladanke(nowy_stan)
                kolejka.append((nowy_stan, historia + [ruch], g))

    print("Nie znaleziono rozwiązania :(")
    return None


# Rozpocznij program
if __name__ == "__main__":
    startowy_stan = " 13425786"
    print("START:")
    pokaz_ukladanke(startowy_stan)
    szukaj_rozwiazania(startowy_stan)
