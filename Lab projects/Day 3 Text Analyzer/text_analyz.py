def freq(count):
    val_lst = list(count.values())
    if max(val_lst) == 1:
        return 0
    return list(count.keys())[val_lst.index(max(val_lst))]


to_read_from = open("text.txt", "r").read()
to_write = open("new_text.txt", "w")
to_read = to_read_from.split()
count_let, count_word = {}, {}
for word in to_read:
    count_word[word] = count_word.get(word, 0) + 1
for word in to_read:
    for i in word:
        if i.isalpha():
            count_let[i] = count_let.get(i, 0) + 1
to_write.write(f"Words: {len(to_read)} \nLetters: {len(count_let)} \nSentences: {to_read_from.count('.')}"
               f" \nLetter frequency: {freq(count_let)} \nWords frequency: {freq(count_word)}")
to_write.close()
