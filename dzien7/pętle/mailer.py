import smtplib
from zajeciaPyt4.dzien7.secrets import *

adresat = login
nadawca = login
haslo = haslo

#tworzenie silnik mailera
mailer = smtplib.SMTP("smtp.gmail.com", 587)
#witam się z serwerem/ łączę się
mailer.ehlo()
#szyfruje połączenie
mailer.starttls()
#loguje się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Daniel\n"
wiadomosc = "To jest moja wiadomosc"
tresc = temat + wiadomosc

#wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila!")

mailer.close()