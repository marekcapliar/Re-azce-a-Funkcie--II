def uloha1(n: int, slovo: str):
    if n >= len(slovo):
        return print('zly index')
    else:
        return print(slovo[n])


uloha1(6, 'kamikadze')
uloha1(3, 'kuk')
uloha1(0, ' ')
uloha1(0, '')
