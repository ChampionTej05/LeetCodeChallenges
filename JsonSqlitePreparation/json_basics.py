import json 


#encode json (serialise the object)

## python obj to json string  

obj = {"a": 1, "b": 2}
data = json.dumps(obj,indent = 4)
print(data)

## file stream to json object 
with open('encoded_file.json', 'w') as f:
    json.dump(obj, f)


# decode json (deserialise object)
    
json_string = """ {"a": 1, "b": 2} """
data = json.loads(json_string)
print(data)

## file stream 

with open('file.json', 'r') as f:
    data = json.load(f)
    print(data)


# incrementally process file 
import ijson

count = 0
'''
The key 'item' is used to specify the path to the items in the JSON document; in this case, each item in the root array.
If structure would have been like this 
{
"agenda":[{
"name" : a,
"age: 12
}]
}
then ijson.items(file, "agends.item")
'''
with open('large_data.json', 'r') as file:
    parser = ijson.items(file, 'item')
    for item in parser:
        if item['age'] > 20:
            count += 1

print(f"Number of instances with age > 20: {count}")
