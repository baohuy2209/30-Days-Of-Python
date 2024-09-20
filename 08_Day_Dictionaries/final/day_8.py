empty_dict = {}
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dct)
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person)
print(len(person))
print(dct["key1"])
print(dct["key4"])
print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])
# print(person["city"])
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person.get("first_name"))  # Asabeneh
print(person.get("country"))  # Finland
print(
    person.get("skills")
)  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get("get"))
dct["key5"] = "value5"
print(dct)

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person["job_title"] = "Intructor"
person["skills"].append("HTML")
print(person)
dct["key1"] = "value-one"
print(dct)
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person["first_name"] = "Eyob"
person["age"] = 252
print(person)
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print("key2" in dct)  # True
print("key5" in dct)  # False

dct.pop("key1")
print(dct)
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.popitem()
print(dct)
