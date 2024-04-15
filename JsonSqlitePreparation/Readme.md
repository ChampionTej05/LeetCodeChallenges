
# Python JSON Basics 

Reference  : https://docs.python.org/3/library/json.html

## Encoding JSON [ PYTHON OBJ -> JSON String ]

### For Python Objects (json.dumps())

- Extra params useful here are `indent=4` to pretty print 
- `sort_keys=True` to sort the Json object 

```python
import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
--> '["foo", {"bar": ["baz", null, 1.0, 2]}]'
```


### For Python file objects (json.dump())

```python
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
--> '["streaming API"]'
```



## Decoding JSON [ JSON STRING -> PYTHON OBJ ]

### For JSON Strings (json.loads())

```python
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]
```

### For JSON File Stream (json.load())

```python 
from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)
--> ['streaming API']
```
