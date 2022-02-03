from src import NestedObject

sample_dict = { "k1":"v1", "k2":[{"a1":"v2","a2":"v3"},{"a1":"v4","a2":"v5"}]}

d2 = NestedObject(sample_dict)
d2.data
print(f"All available paths :{d2.paths}")   # List of all available paths ['/k1', '/k2', '/k2[0]', '/k2[0]/a1', '/k2[0]/a2', '/k2[1]', '/k2[1]/a1', '/k2[1]/a2']
print(f"All available keys (similar to dict.keys()): {d2.keys()}")  # List of keys Similar to .keys method in dict ['/k1', '/k2', '/k2[0]', '/k2[0]/a1', '/k2[0]/a2', '/k2[1]', '/k2[1]/a1', '/k2[1]/a2']
print(f"All available key value pairs as a tuple(): {d2.items()}") 
    # list of tuples Similar to the items method in a normal dictionary
    # [('/k1', 'v1'), ('/k2', [{'a1': 'v2', 'a2': 'v3'}, {'a1': 'v4', 'a2': 'v5'}]), ('/k2[0]', {'a1': 'v2', 'a2': 'v3'}), ('/k2[0]/a1', 'v2'), ('/k2[0]/a2', 'v3'), ('/k2[1]', {'a1': 'v4', 'a2': 'v5'}), ('/k2[1]/a1', 'v4'), ('/k2[1]/a2', 'v5')]
print(f"Get value from keypath '/k2' : {d2.get(keypath='/k2')}")   
    # Tuple with (key, value)  where key is the keypath
    # ('/k2', [{'a1': 'v2', 'a2': 'v3'}, {'a1': 'v4', 'a2': 'v5'}])
print(f"Get value from i keypath '/k2[i]/a1' : {d2.get(keypath='/k2[i]/a1')}") 
    # List of tuple with i replaced with length of list in k2 key
    # [('/k2[0]', {'a1': 'v2', 'a2': 'v3'}), ('/k2[1]', {'a1': 'v4', 'a2': 'v5'})]