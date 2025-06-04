from boyer_moore import boyer_moore_search

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

def split_into_sentences(text):
    sentences = []
    sentence = ""
    end_marks = [".", "!", "?"]

    for char in text:
        sentence += char
        if char in end_marks:
            sentences.append(sentence.strip())
            sentence = ""

    if sentence.strip():
        sentences.append(sentence.strip())

    return sentences

sentences = split_into_sentences(text)

dollar_sentences = []

for sentence in sentences:
    if boyer_moore_search(sentence, "грн"):
        dollar_sentences.append(sentence)
        print(sentence)
for sentence in sentences:
    if boyer_moore_search(sentence, "$"):
        dollar_sentences.append(sentence)
        print(sentence)
