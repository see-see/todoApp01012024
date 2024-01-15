car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()


print(list(x), id(x))

car["year"] = 2018

print(x, id(x))
