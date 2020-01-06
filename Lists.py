x = ["Alicja", "Marcin", "Zygmunt"]
print(len(x))
# x.append("zbigniew")
print(len(x))
x.remove("marcin")
for i, y in enumerate(x):
    print("Element i", i, ": ", y)

if "zbigniew" in x:
    print("Zbigniew jest na Liście")
else:
    print("Nie ma Zbigniewa na Liście")