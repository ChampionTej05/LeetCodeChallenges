import json
from typing import Any 

class Person:

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender


class PersonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        
        if isinstance(o, Person):
            return {"name": o.name, "age": o.age, "gender": o.gender}
        return json.JSONEncoder.default(self, o)

def custom_person_decoder(obj):
    if "name" in obj and "age" in obj and "gender" in obj:
        return Person(obj["name"], obj["age"], obj["gender"])
    return obj

person = Person("Rakshit", 25 , "Male")

# without custom json encoder 
# data = json.dumps(person)
# print(data)
# TypeError: Object of type Person is not JSON serializable

#with custom encoder 
data = json.dumps(person , cls= PersonEncoder)
print(data)


#decoding using custom decoder 

person_decoded = json.loads(data, object_hook=custom_person_decoder)
print(person_decoded)



