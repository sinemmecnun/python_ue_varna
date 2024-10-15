# Прочетете от конзолата абзац (изречения, завършващи с точка) и запишете текста в списък по изречения.
# Прочетете от конзолата дума, която да се търси в подадения текст. Ако тази дума я има в някое изречение,
# изведете изречението. Прочетете от конзолата дума с която да се замени предишно въведената дума. Изведете целия абзац с заменената дума

# Прочетете от конзолата абзац (изречения, завършващи с точка) и запишете текста в списък по изречения.
text = input().split('. ')
print(text)

# Прочетете от конзолата дума, която да се търси в подадения текст. Ако тази дума я има в някое изречение,
# изведете изречението.
word_to_find = input()

for sentence in text:
    if word_to_find in sentence:
        print(sentence)

[print(s) for s in text if word_to_find in s]

# Прочетете от конзолата дума с която да се замени предишно въведената дума
word_to_replace = input()

new_text = []

for sentence in text:
    new_text.append(sentence.replace(word_to_find, word_to_replace))

for index in range(len(text)):
    if word_to_find in text[index]:
        text[index] = text[index].replace(word_to_find, word_to_replace)

print(', '.join(text))

# Изведете целия абзац с заменената дума
print('. '.join(new_text))
