def countslov(text):
    words = text.split()
    count = 0
    for word in words:
        if word.endswith("я") or word.endswith("я"):
            count += 1
    return count

text = "Змея лодка семья карта шар скамья"
res= countslov(text)
print("Количество слов, заканчивающихся на букву 'я':", res)