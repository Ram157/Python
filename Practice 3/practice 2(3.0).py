from collections import Counter
def stat(text):
    text = str(text)
    counter = Counter(text)
    if not counter:
        print('Нет символов для анализа')
        return
    top3 = counter.most_common(3)
    print('ТОП 3 САМЫХ ВСТРЕЧАЮЩИХСЯ:', top3)
    print('КОЛИЧЕСТВО ВСЕХ СИМВОЛОВ: ', counter.items())
stat('sddasaaa ss')