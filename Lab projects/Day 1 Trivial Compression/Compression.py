to_read = open("text.txt", "r").read()
to_write = open("new_text.txt", "w")
dict_2 = {"th": "0",
          "he": "1",
          "in": "2",
          "er": "3",
          "an": "4",
          "re": "5",
          "nd": "6",
          "on": "7",
          "en": "8",
          "at": "9",
          "ou": ")",
          "ed": "(",
          "ha": "[",
          "to": "]",
          "or": "{",
          "it": "}",
          "is": "@",
          "hi": "#",
          "es": "$",
          "ng": "^"
          }
dict_3 = {"the": "!0",
          "and": "!1",
          "ing": "!2",
          "her": "!3",
          "hat": "!4",
          "his": "!5",
          "tha": "!6",
          "ere": "!7",
          "for": "!8",
          "ent": "!9",
          "ion": "?0",
          "ter": "?1",
          "was": "?2",
          "you": "?3",
          "ith": "?4",
          "ver": "?5",
          "all": "?6",
          "wit": "?7",
          "thi": "?8",
          "tio": "?9"
          }
dict_4 = {"this": "_0",
          "that": "_1",
          "ther": "_2",
          "with": "_3",
          "have": "_4",
          "tion": "_5",
          "here": "_6",
          "ould": "_7",
          "ight": "_8",
          "hich": "_9",
          "whic": "-0",
          "thin": "-1",
          "they": "-2",
          "atio": "-3",
          "ever": "-4",
          "from": "-5",
          "ough": "-6",
          "were": "-7",
          "hing": "-8",
          "ment": "-9"
          }
for i in dict_4:
    to_read = to_read.replace(i, dict_4[i])
for i in dict_3:
    to_read = to_read.replace(i, dict_3[i])
for i in dict_2:
    to_read = to_read.replace(i, dict_2[i])
to_write.write(to_read)
to_write.close()
