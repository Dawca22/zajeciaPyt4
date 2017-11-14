rzeczy = ["donicza", "kwiatek", "ziemia", "woda"]

# append dodaje na sam koniec
rzeczy.append("konewka")
rzeczy.append("grabie")
rzeczy.append("konewka")

print(rzeczy)

if "konewka" in rzeczy:
    rzeczy.remove("konewka")

print(rzeczy)