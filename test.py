NorthAmerica = ["Alaska","Northwest_Territory","Greenland","Alberta","Ontario","Quebec","Western United States","Eastern_United_States","Central_America"]
SouthAmerica = ["Venezuela","Peru","Brasil","Argentina"]
Africa = ["North Africa","Egypt","Congo","South Africa","Madagascar","East_Africa"]
Europe = ["Iceland","Scandinavia","Ukraine","Great_Britain","Northern_Europe","Southern_Europe","Western_Europe"]
Australia = ["Indonesia","New Guinea","Western Australia","Eastern_Australia"]
Asia = ["Siam","India","China","Mongolia","Japan","Irkutsk","Yakutst","Kamchatka","Siberia","Afghanistan","Ural","Middle_East"]

my =  ["Venezuela","Peru","Brasil","Argentina","North Africa","Egypt","Congo","South Africa","Madagascar","East_Africa"]

if(all(x in my for x in SouthAmerica)):
    print("YUP")
