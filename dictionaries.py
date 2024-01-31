#creating a dict
dict1={'x':10,'y':20,'z':30}
print(dict1)
print(type(dict1))

#accessing dict
print(dict1['x'])
print(dict1['y'])

#dict methods
print(len(dict1))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.update({'s':45}))
print(dict1.popitem())
print(dict1.pop('x'))

#second dict copied
dict2=dict1.copy()
print(dict2)

print(dict1.clear())
