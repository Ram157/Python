from collections import Counter
def stat(text):
    text = str(text)
    counter = Counter(text)
    print(counter.total)
stat('sdas')