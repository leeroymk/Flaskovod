def solution():
    x: list = input().split()
    res: list = []
    lack_words: int = 0
    for var in x:
        res.append(var) if var.isalpha() else res.clear()
        if len(res) == 2:
            lack_words += 1
            print(*res)
    if lack_words == 0:
        print('Мало букв!')


solution()
