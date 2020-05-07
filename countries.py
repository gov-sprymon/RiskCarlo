countries_dict = dict()

startingUnitCount = 3

countries_dict["Alaska"] = [
                        ["Northwest_Territory",
                        "Alberta",
                        "Kamchatka"
                        ],startingUnitCount,0,"North America"]
countries_dict["Northwest_Territory"] = [
                        ["Alaska",
                        "Alberta",
                        "Greenland",
                        "Ontario"
                        ],startingUnitCount,1,"North America"]
countries_dict["Greenland"] =[
                        ["Northwest_Territory",
                        "Ontario",
                        "Quebec",
                        "Iceland"
                        ],startingUnitCount,0,"North America"]

countries_dict["Alberta"] = [
                        ["Alaska",
                        "Northwest_Territory",
                        "Western_United_States",
                        "Ontario"
                        ],
                        startingUnitCount,1,"North America"]
countries_dict["Ontario"] = [
                        ["Northwest_Territoty",
                        "Greenland","Quebec",
                        "Eastern_United_States",
                        "Western_United_States",
                        "Alberta"
                        ],startingUnitCount,0,"North America"]
countries_dict["Quebec"] = [
                        ["Greenland",
                        "Ontario",
                        "Eastern_United_States"
                        ],startingUnitCount,1,"North America"]
countries_dict["Western_United_States"] = [
                        ["Alberta",
                        "Ontario",
                        "Eastern_United_States",
                        "Central_America"
                        ],startingUnitCount,0,"North America"]
countries_dict["Eastern_United_States"] = [
                        ["Western_United_States",
                        "Central_America",
                        "Ontario",
                        "Quebec"
                        ],startingUnitCount,1,"North America"]
countries_dict["Central_America"] = [
                        ["Western_United_States",
                        "Eastern_United_States",
                        "Venezuela"
                        ],startingUnitCount,0,"North America"]


#SOUTH AMERICA
countries_dict["Venezuela"] = [
                        ["Central_America",
                        "Peru",
                        "Brasil"
                        ],startingUnitCount,1,"South America"]
countries_dict["Peru"] = [
                        ["Venezuela",
                        "Brasil",
                        "Argentina"
                        ],startingUnitCount,0,"South America"]
countries_dict["Brasil"] = [
                        ["Venezuela",
                        "Peru",
                        "Argentina",
                        "North_Africa"
                        ],startingUnitCount,1,"South America"]
countries_dict["Argentina"] = [
                        ["Brasil",
                        "Peru"
                        ],startingUnitCount,0,"South America"]


#AFRICA
countries_dict["North_Africa"] = [
                        ["Western_Europe",
                        "Southern_Europe",
                        "Egypt",
                        "East_Africa",
                        "Congo",
                        "Brasil"
                        ],startingUnitCount,1,"Africa"]
countries_dict["Egypt"] = [
                        ["Middle_East",
                        "Southern_Europe",
                        "North_Africa",
                        "East_Africa"
                        ],startingUnitCount,0,"Africa"]
countries_dict["East_Africa"] = [
                        [
                        "South_Africa",
                        "Egypt",
                        "North_Africa",
                        "Congo",
                        "Madagascar"
                        ],startingUnitCount,1,"Africa"]
countries_dict["Congo"] = [
                        [
                        "North_Africa",
                        "South_Africa",
                        "East_Africa"
                        ],startingUnitCount,0,"Africa"]
countries_dict["South_Africa"] = [
                        ["Madagascar",
                        "East_Africa",
                        "Congo"
                        ],startingUnitCount,1,"Africa"]
countries_dict["Madagascar"] = [
                        ["East_Africa",
                        "South_Africa"
                        ],startingUnitCount,0,"Africa"]


#EUROPE
countries_dict["Iceland"] = [
                        ["Greenland",
                        "Scandinavia",
                        "Great_Britain"
                        ],startingUnitCount,1,"Europe"]
countries_dict["Scandinavia"] = [
                        ["Iceland",
                        "Northern_Europe",
                        "Great_Britain",
                        "Ukraine"
                        ],startingUnitCount,0,"Europe"]
countries_dict["Ukraine"] = [
                        ["Ural",
                        "Scandinavia",
                        "Afghanistan",
                        "Middle_East",
                        "Southern_Europe",
                        "Northern_Europe"
                        ],startingUnitCount,1,"Europe"]
countries_dict["Great_Britain"] = [
                        ["Scandinavia",
                        "Iceland",
                        "Northern_Europe",
                        "Western_Europe"
                        ],startingUnitCount,0,"Europe"]
countries_dict["Northern_Europe"] = [
                        ["Great_Britain",
                        "Scandinavia",
                        "Southern_Europe",
                        "Western_Europe",
                        "Ukraine"
                        ],startingUnitCount,1,"Europe"]
countries_dict["Southern_Europe"] = [
                        [
                        "Middle_East",
                        "Ukraine",
                        "Northern_Europe",
                        "Egypt",
                        "North_Africa",
                        "Western_Europe"
                        ],startingUnitCount,0,"Europe"]
countries_dict["Western_Europe"] = [
                        ["North_Africa",
                        "Southern_Europe",
                        "Great_Britain",
                        "Northern_Europe"
                        ],startingUnitCount,1,"Europe"]

#AUSTRALIA
countries_dict["Indonesia"] = [
                        ["Siam",
                        "New_Guinea",
                        "Western_Australia"
                        ],startingUnitCount,0,"Australia"]
countries_dict["New_Guinea"] = [
                        ["Indonesia",
                        "Eastern_Australia",
                        "Western_Australia"
                        ],startingUnitCount,1,"Australia"]
countries_dict["Western_Australia"] = [
                        ["Indonesia",
                        "New_Guinea",
                        "Eastern_Australia"
                        ],startingUnitCount,0,"Australia"]
countries_dict["Eastern_Australia"] = [
                        ["New_Guinea",
                        "Western_Australia"
                        ],startingUnitCount,1,"Australia"]

#ASIA
countries_dict["Siam"] = [
                        ["Indonesia",
                        "China",
                        "India"
                        ],startingUnitCount,0,"Asia"]
countries_dict["India"] = [
                        ["Siam",
                        "China",
                        "Afghanistan",
                        "Middle_East"
                        ],startingUnitCount,1,"Asia"]
countries_dict["China"] = [
                        ["Siam",
                        "Mongolia",
                        "India",
                        "Siberia",
                        "Ural",
                        "Afghanistan"
                        ],startingUnitCount,0,"Asia"]
countries_dict["Mongolia"] = [
                        ["Irkutsk",
                        "Mongolia",
                        "Siberia",
                        "Kamchatka",
                        "Japan"
                        ],startingUnitCount,1,"Asia"]
countries_dict["Japan"] = [
                        ["Mongolia",
                        "Kamchatka"
                        ],startingUnitCount,0,"Asia"]
countries_dict["Irkutsk"] = [
                        ["Mongolia",
                        "Kamchatka",
                        "Yakutst",
                        "Siberia",
                        ],startingUnitCount,1,"Asia"]
countries_dict["Yakutst"] = [
                        ["Kamchatka",
                        "Irkutsk",
                        "Siberia"
                        ],startingUnitCount,0,"Asia"]
countries_dict["Kamchatka"] = [
                        ["Alaska",
                        "Yakutst",
                        "Irkutsk",
                        "Mongolia",
                        "Japan"
                        ],startingUnitCount,1,"Asia"]
countries_dict["Siberia"] = [
                        ["Ural",
                        "Yakutst",
                        "Irkutsk",
                        "China",
                        "Mongolia"
                        ],startingUnitCount,0,"Asia"]
countries_dict["Afghanistan"] = [
                        ["Ukraine",
                        "Ural",
                        "China",
                        "India",
                        "Middle_East"
                        ],startingUnitCount,1,"Asia"]
countries_dict["Ural"] = [
                        ["Siberia",
                        "Ukraine",
                        "Afghanistan",
                        "China"
                        ],startingUnitCount,0,"Asia"]
countries_dict["Middle_East"] = [
                        ["Egypt",
                        "India",
                        "Afghanistan",
                        "Ukraine",
                        "Southern_Europe"
                        ],startingUnitCount,1,"Asia"]

NorthAmerica = ["Alaska","Northwest_Territory","Greenland","Alberta","Ontario","Quebec","Western_United_States","Eastern_United_States","Central_America"]
SouthAmerica = ["Venezuela","Peru","Brasil","Argentina"]
Africa = ["North_Africa","Egypt","Congo","South_Africa","Madagascar","East_Africa"]
Europe = ["Iceland","Scandinavia","Ukraine","Great_Britain","Northern_Europe","Southern_Europe","Western_Europe"]
Australia = ["Indonesia","New_Guinea","Western_Australia","Eastern_Australia"]
Asia = ["Siam","India","China","Mongolia","Japan","Irkutsk","Yakutst","Kamchatka","Siberia","Afghanistan","Ural","Middle_East"]
