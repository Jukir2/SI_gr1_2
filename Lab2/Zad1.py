from collections import deque

def czy_cel(stan):
    return (stan[1] == 'czysto' and stan[2] == 'czysto')

def wykonaj_akcje(stan, akcja):
    lokacja, stanA, stanB = stan

    if akcja == 'Lewo' and lokacja == 'B':
        return ('A', stanA, stanB)
    if akcja == 'Prawo' and lokacja == 'A':
        return ('B', stanA, stanB)
    if akcja == 'Odkurzaj':
        if lokacja == 'A':
            return ('A', 'czysto', stanB)
        else:
            return ('B', stanA, 'czysto')
    if akcja == 'NicNieRob':
        return stan

    return stan

def bfs_debug(stan_poczatkowy):
    print("====================")
    print(f"START: {stan_poczatkowy} (alias: s1)")
    print("====================")

    if czy_cel(stan_poczatkowy):
        print("Stan początkowy to już stan docelowy!")
        return ['NicNieRob']

    kolejka = deque([(stan_poczatkowy, [], 's1')])
    odwiedzone = {stan_poczatkowy}
    aliasy = {'s1': stan_poczatkowy}
    alias_counter = {'s1': 0}
    alias_sciezka = {'s1': []}  # przechowuje aliasową ścieżkę

    while kolejka:
        print("--------------------")
        stan, sciezka, alias = kolejka.popleft()
        print(f"[{alias}] Obecny stan: {stan}")

        if czy_cel(stan):
            print(f">>> OSIĄGNIĘTO CEL w {alias}!\n")
            print("Sekwencja akcji prowadząca do celu:")
            print(" -> ".join(sciezka))

            print("\nŚcieżka aliasów do celu:")
            print(" -> ".join(alias_sciezka[alias] + [alias]))

            print("\nStan końcowy:", stan)
            print("====================")
            return sciezka

        print("Możliwe akcje:")
        for a in ['Lewo', 'Prawo', 'Odkurzaj']:
            nowy_stan = wykonaj_akcje(stan, a)
            status = '✓ NOWY' if nowy_stan not in odwiedzone else '✗ już odwiedzony'

            if nowy_stan not in odwiedzone:
                if alias not in alias_counter:
                    alias_counter[alias] = 0
                alias_counter[alias] += 1
                nowy_alias = alias + str(alias_counter[alias])
                aliasy[nowy_alias] = nowy_stan
                alias_sciezka[nowy_alias] = alias_sciezka[alias] + [alias]

                odwiedzone.add(nowy_stan)
                kolejka.append((nowy_stan, sciezka + [a], nowy_alias))
                print(f" - {a} -> {nowy_stan} ({status}) → alias: {nowy_alias}")
            else:
                print(f" - {a} -> {nowy_stan} ({status})")

    print("Nie znaleziono rozwiązania.")
    return []

# Uruchomienie
if __name__ == "__main__":
    stan_startowy = ('A', 'brudno', 'brudno')
    wynik = bfs_debug(stan_startowy)