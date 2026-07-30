country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}
country_capitals["Italy"] = "Rome"
del country_capitals["Germany"]
print(country_capitals)
for country in country_capitals:
    print(country)
print()
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
