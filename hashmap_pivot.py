def hashmap_pivot(entries):
    hashmap = {}
    for category in entries:
        for key_value in category.split(", "):
            key, value = key_value.split(": ")
            hashmap.setdefault(key+"s",[]).append(value)
    return hashmap

entries = [
    "id: 1, name: Alice, age: 20, grade: A",
    "id: 2, name: Bob, age: 22, grade: B",
    "id: 3, name: Charlie, age: 21, grade: A"
]
print(hashmap_pivot2(entries))