
while True:
    try:
        fish = float(input("Mikä on kuhasi pituus centtimetreinä?: "))
    except ValueError:
        print("Syötä pelkkä numero, desimaalit ovat sallittua.")
        continue
    else:
        break

if fish <= 37:
    size_diff = 37 - fish
    print("Laskea kuhasi takaisin veteen, se on " + str(size_diff) + "cm liian lyhyt.")
else:
    print("Kuhasi on tarpeeksi iso. :)")