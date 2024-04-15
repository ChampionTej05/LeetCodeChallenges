import json

class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class Person:
    def __init__(self, name, addresses):
        self.name = name
        self.addresses = addresses


def decode_complex(obj):
    if "type" not in obj:
        return obj

    if obj["type"] == "person":
        return Person(name=obj["name"], addresses=obj.get("addresses", []))
    elif obj["type"] == "address":
        return Address(city=obj["city"], country=obj["country"])

    return obj

# type is added to each dict, to identify the type of object each dict uses
person_json = '''{
  "type": "person",
  "name": "Alice",
  "addresses": [
    {
      "type": "address",
      "city": "New York",
      "country": "USA"
    }
  ]
}'''

person = json.loads(person_json, object_hook=decode_complex)