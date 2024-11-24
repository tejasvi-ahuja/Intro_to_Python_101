marks = {
    "Harry": 100,
    "Garry": 56,
    "Larry": 23
}

# print(marks, type(marks))
print(marks["Garry"])

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry": 99})
print(marks)

print(marks.get("Harry2"))

