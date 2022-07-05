countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
count=0
for i in countries.items():
    if city in i[1]:
        print(f'INFO: {city} is a city in {i[0]}')
        break
    else:
        count+=1
if count==5:
    print(f'ERROR: Country for {city} not found')