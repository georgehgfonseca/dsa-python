# Design a key-value store that allows three operations

# setKet(key, value)
# Sets key with value

# setSum(key, values)
# Sets key as the sum of the values that are a set of keys
# Q. Values can be another key composed by the sum of other keys and so on
# Q. A key reference can be updated changing the key's value

# getKey(key)
# Returns the value of the key
# Q. If key does not exist, return 0

# setKey('A', 3)
# setKey('B', 5)
# getKey('A') -> 3
# setSum('C', ['A', 'B'])
# getKey('C') -> 8
# setKey('A', 1)
# getKey('C') -> 6
# setSum('D', ['C', 'B'])
# getKey('D') -> 11