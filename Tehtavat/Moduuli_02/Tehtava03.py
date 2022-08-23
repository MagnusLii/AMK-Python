width = float(input("Syötä kannan pituus: "))
height = float(input("Syötä korkeus: "))

area = str(round(width*height,2))
perimeter = str(round(height*2+width*2,2))

print("Suorakulmion alue on " +area +" ykksikköä, ja piiri on " +perimeter +" ykksikköä.")