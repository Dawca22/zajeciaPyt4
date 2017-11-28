import zajeciaPyt4.dzien7.moj_modul.odwrocony_string


def czy_palindrom(wyraz):
    """Sprawdzaczy podany string jest palindromem
    (str)>bool"""

    odwrocony = dzien7.moj_modul.odwrocony_string.odwroc_sting(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False

print(czy_palindrom("kajak"))