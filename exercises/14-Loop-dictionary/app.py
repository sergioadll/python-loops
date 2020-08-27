
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }
add_words={'love' : "amor", "code" : "codigo","smart" : "inteligente"}
spanish_translations.update(add_words)

print("All", spanish_translations)
for key in spanish_translations:
    print(key, " -> ", spanish_translations[key])
