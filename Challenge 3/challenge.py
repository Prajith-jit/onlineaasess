#Function to find the value based on the key
def find(key, value):
  for k, v in (value.items() if isinstance(value, dict) else
               enumerate(value) if isinstance(value, list) else []):
    if k == key:
      return v
    elif isinstance(v, (dict, list)):
      for result in find(key, v):
        return result


item = {"a": 1, 'b': [2, 3, {"c": 100}]}
item1 = {"a":{"b":{"c":"d"}}}


value=find("a", item1)
print(value)