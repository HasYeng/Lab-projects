to_read = open("new_text.txt", "r").read()
to_write = open("decomp.txt", "w")
dict_2 = {"0": "th",
          "1": "he",
          "2": "in",
          "3": "er",
          "4": "an",
          "5": "re",
          "6": "nd",
          "7": "on",
          "8": "en",
          "9": "at",
          ")": "ou",
          "(": "ed",
          "[": "ha",
          "]": "to",
          "{": "or",
          "}": "it",
          "@": "is",
          "#": "hi",
          "$": "es",
          "^": "ng"
          }
dict_3 = {"!0": "the",
          "!1": "and",
          "!2": "ing",
          "!3": "her",
          "!4": "hat",
          "!5": "his",
          "!6": "tha",
          "!7": "ere",
          "!8": "for",
          "!9": "ent",
          "?0": "ion",
          "?1": "ter",
          "?2": "was",
          "?3": "you",
          "?4": "ith",
          "?5": "ver",
          "?6": "all",
          "?7": "wit",
          "?8": "thi",
          "?9": "tio"
          }
dict_4 = {"_0": "this",
          "_1": "that",
          "_2": "ther",
          "_3": "with",
          "_4": "have",
          "_5": "tion",
          "_6": "here",
          "_7": "ould",
          "_8": "ight",
          "_9": "hich",
          "-0": "whic",
          "-1": "thin",
          "-2": "they",
          "-3": "atio",
          "-4": "ever",
          "-5": "from",
          "-6": "ough",
          "-7": "were",
          "-8": "hing",
          "-9": "ment"
          }
for i in dict_4:
    to_read = to_read.replace(i, dict_4[i])
for i in dict_3:
    to_read = to_read.replace(i, dict_3[i])
for i in dict_2:
    to_read = to_read.replace(i, dict_2[i])
to_write.write(to_read)
to_write.close()
