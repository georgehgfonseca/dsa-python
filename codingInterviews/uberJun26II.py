# Design a key-value store that allows three operations. All operations must run in ammortized constant time (O(1)).

# put("Mario", "Nintendo")
# put("Delta", "Bravo")
# put("Brazil", "Country")
# get("Delta") -> "Bravo"

# kv = {"Mario": {"value": "Nintendo", "key_index": 0}, "Delta": {"value": "Bravo", "key_index": 1}, "Brazil": {"value": "Country", "key_index": 2}}
# keys = ['Mario', 'Delta', 'Brazil']

# getRandom() -> ("Mario", "Nintendo") or ("Delta", "Bravo") or ("Brazil", "Country")


# Q. What is expected when calling put on an existing key? Replace 
# Q. What is expected when calling get on missing key? Throw error/exception
# Q. Can values be other than string? Yes
# Q. I'm allowed to use builtin random? Yes

# Follow-up implement remove operation 

class KVStore():
    def __init__(self):
        self.kv = dict()
        self.keys = []

    def put(self, key, value):
        index = len(self.keys) if key not in self.kv else self.kv[key]["index"]
        if key not in self.kv:
            self.keys.append(key)

        self.kv[key] = {"value": value, "index": index}

    def get(self, key):
        if key not in self.kv:
            raise ValueError("Key not found")
        
        return self.kv[key]["value"]
    
    def getRandom(self):
        import random
        random_key = self.keys[random.randint(0, len(self.keys) - 1)]
        return (random_key, self.kv[random_key]["value"])

    def remove(self, key):
        key_index = self.kv[key]["index"]
        swapped_key = self.keys[-1]
        self.keys[-1], self.keys[key_index] = self.keys[key_index], self.keys[-1]
        self.keys.pop()

        self.kv.pop(key)
        self.kv[swapped_key]["index"] = key_index

# Test cases
kv = KVStore()
kv.put("Mario", "Nintendo")
kv.put("Delta", "Bravo")
kv.put("Brazil", "Country")
assert kv.get("Delta") == "Bravo"
print(kv.getRandom(), kv.getRandom(), kv.getRandom())
assert kv.kv == {"Mario": {"value": "Nintendo", "index": 0}, "Delta": {"value": "Bravo", "index": 1}, "Brazil": {"value": "Country", "index": 2}}
assert kv.keys == ['Mario', 'Delta', 'Brazil']
kv.remove("Delta")
assert kv.kv == {"Mario": {"value": "Nintendo", "index": 0}, "Brazil": {"value": "Country", "index": 1}}
assert kv.keys == ['Mario', 'Brazil']

try:
    kv.get("Delta")
except ValueError:
    pass

