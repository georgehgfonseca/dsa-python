# Design a key-value dictionary that allows three operations

# setKet(key, value)
# Sets key with value

# setSum(key, values)
# Sets key as the sum of the values that are a set of keys
# Q. Values can be another key composed by the sum of other keys and so on

# getKey(key)
# Returns the value of the key
# Q. If key does not exist, return 0

# setKey('A', 1)
# setKey('B', 2)
# getKey('A') -> 1
# setKey('C', ['A', 'B'])
# getKey('C') -> 3