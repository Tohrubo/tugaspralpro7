word = "mata"
chklist = ["ama", "maat", "taas", "tama"]

sortword = sorted(word)

for item in chklist:
    chkw = sorted(item)
    if chkw == sortword:
        print(f"{item} is an Anagram of {word}")
    else:
        print(f"{item} is not an Anagram of {word}")