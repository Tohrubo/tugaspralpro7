snt = "Saya mau makan. Makan itu wajib, Mau siang atau malam saya wajib makan."
search = "makan"

snt = snt.lower()
sntlist = snt.split()
count = 0

for item in sntlist:
    word = ''.join([j for j in item if j.isalpha()])
    if word == search:
        count += 1

print(f"{search} Muncul {count} kali")