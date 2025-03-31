import numpy as np

# Drzewo gry jako słownik, gdzie klucz to węzeł, a wartość to dzieci lub wartość użytkowa
# Węzły wewnętrzne mają listę dzieci, a liście mają przypisane wartości końcowe

drzewo_gry = {
    'A': ['B', 'C', 'D'],
    'B': ['b1', 'b2', 'b3'],
    'C': ['c1', 'c2', 'c3'],
    'D': ['d1', 'd2', 'd3'],
    'b1': 3, 'b2': 12, 'b3': 8,
    'c1': 2, 'c2': 4, 'c3': 6,
    'd1': 14, 'd2': 2, 'd3': 2
}

# Algorytm Minimax z przycinaniem Alpha-Beta, zwracający także optymalną ścieżkę

def minimax_alpha_beta(wezel, alpha, beta, czy_max, sciezka, poziom=0):
    """
    Funkcja rekurencyjna implementująca algorytm Minimax z przycinaniem Alpha-Beta.

    Parametry:
    - wezel: aktualnie analizowany węzeł w drzewie gry
    - alpha: najlepsza znaleziona wartość dla gracza MAX (największa)
    - beta: najlepsza znaleziona wartość dla gracza MIN (najmniejsza)
    - czy_max: flaga określająca, czy ruch należy do gracza MAX (True) czy MIN (False)
    - sciezka: lista przechowująca przebytą ścieżkę
    - poziom: poziom zagłębienia w drzewie (do estetycznego formatowania)
    """

    wciecie = "  " * poziom  # Tworzenie wcięć dla lepszej czytelności wyjścia
    print(f"{wciecie}- Wejscie do wezla {wezel} (alpha={alpha:.2f}, beta={beta:.2f}, MAX={czy_max})")

    # Sprawdzamy, czy dany węzeł jest liściem (czy ma przypisaną wartość końcową)
    if isinstance(drzewo_gry[wezel], int):
        print(f"{wciecie}- Węzeł {wezel} jest liściem o wartości {drzewo_gry[wezel]}")
        return drzewo_gry[wezel], sciezka + [wezel]

    # Jeśli ruch należy do gracza MAX (maksymalizujemy wartość)
    if czy_max:
        najlepsza_wartosc = -np.inf
        najlepsza_sciezka = []
        for dziecko in drzewo_gry[wezel]:
            print(f"{wciecie}Sprawdzam dziecko {dziecko}")
            wartosc, sciezka_dziecka = minimax_alpha_beta(dziecko, alpha, beta, False, sciezka + [wezel], poziom + 1)

            # Aktualizacja najlepszej wartości
            if wartosc > najlepsza_wartosc:
                najlepsza_wartosc = wartosc
                najlepsza_sciezka = sciezka_dziecka

            # Aktualizacja wartości Alpha (najlepsza znaleziona wartość dla MAX)
            alpha = max(alpha, najlepsza_wartosc)
            print(f"{wciecie}Aktualizacja {wezel}: najlepsza_wartosc={najlepsza_wartosc}, alpha={alpha:.2f}, beta={beta:.2f}")

            # Przycinanie gałęzi drzewa (jeśli Beta <= Alpha, nie ma sensu przeszukiwać dalej)
            if beta <= alpha:
                print(f"{wciecie}Przycinanie w wezle {wezel} (beta <= alpha)")
                break
        return najlepsza_wartosc, najlepsza_sciezka

    # Jeśli ruch należy do gracza MIN (minimalizujemy wartość)
    else:
        najlepsza_wartosc = np.inf
        najlepsza_sciezka = []
        for dziecko in drzewo_gry[wezel]:
            print(f"{wciecie}Sprawdzam dziecko {dziecko}")
            wartosc, sciezka_dziecka = minimax_alpha_beta(dziecko, alpha, beta, True, sciezka + [wezel], poziom + 1)

            # Aktualizacja najlepszej wartości
            if wartosc < najlepsza_wartosc:
                najlepsza_wartosc = wartosc
                najlepsza_sciezka = sciezka_dziecka

            # Aktualizacja wartości Beta (najlepsza znaleziona wartość dla MIN)
            beta = min(beta, najlepsza_wartosc)
            print(f"{wciecie}Aktualizacja {wezel}: najlepsza_wartosc={najlepsza_wartosc}, alpha={alpha:.2f}, beta={beta:.2f}")

            # Przycinanie gałęzi drzewa
            if beta <= alpha:
                print(f"{wciecie}Przycinanie w wezle {wezel} (beta <= alpha)")
                break
        return najlepsza_wartosc, najlepsza_sciezka


# Uruchomienie algorytmu dla korzenia drzewa
print("\nŚledzenie działania algorytmu:")
optymalna_wartosc, optymalna_sciezka = minimax_alpha_beta('A', -np.inf, np.inf, True, [])

# Wyniki końcowe
print("\nOptymalna wartość strategii dla gracza MAX:", optymalna_wartosc)
print("Najlepsza ścieżka ruchów:", " -> ".join(optymalna_sciezka))