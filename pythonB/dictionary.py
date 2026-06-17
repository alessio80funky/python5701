#dictionary  辞書型

a = {
    "brand": "Nissan",
    "model": "carola",
    "year": 2004
}

print(a)#{'brand': 'Nissan', 'model': 'carola', 'year': '2004'}
print(a["brand"])#Nissan
print(a.update({"brand": "Mazda"}))

print(a)#{'brand': 'Mazda', 'model': 'carola', 'year': 2004}
print(a["brand"])#Mazda