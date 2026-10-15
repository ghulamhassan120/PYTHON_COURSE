marks={
    "Harray":100,
    "HAssan":99,
    "Ali":22
}

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Harray":99}))
print(marks.get("Harray")) # None Return 
print(marks["Ali"]) # Error Return
print(marks)