snt = "red snakes and a black frog in the pool"

sntlist = snt.split()
long = 0
short = 1000
res = []

for item in sntlist:
    word = ''.join([i for i in item if i.isalpha()])
    if len(word) > long:
        long = len(word)
        lword = word
    elif len(word) < short:
        short = len(word)
        sword = word

print(f"Shortest word is {sword}")
print(f"Longest word is {lword}")