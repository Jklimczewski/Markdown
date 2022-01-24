import main

def test_dodaj():
    assert dodaj(1, 2) == 3
    assert dodaj(1, 2) == 4
    assert dodaj(1.5, 2) == 3.5


def test_Wypisz():
    assert Wypisz("jabłko") == "Jabłko"
    assert Wypisz("banan") == banan
    assert Wypisz("pies") == Pies
