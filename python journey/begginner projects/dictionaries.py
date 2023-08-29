#dictionaries: key value pairs,unordered, mutable
mydict = {
    "name": "max",
    "age": 28,
    "city": "Newyork"
}
"""print(mydict)

mydict2 = dict(name="Mary", age = 27, city ="newyork")

value = mydict["name"]
print(value)
mydict.popitem()
print(mydict)"""
for key, value in mydict.items:
    print(key, value)

mydict_cpy = mydict


mydict_cpy["email"] = "max@xyz.com"
print()