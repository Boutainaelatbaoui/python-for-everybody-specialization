name = input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != 'From':
        continue
    word = words[1]
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)
