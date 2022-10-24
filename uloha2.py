def uloha2(veta):
    a = '0123456789'
    nt = ''
    for i in veta:
        if i in a:
            nt += i
    return print(len(nt))


uloha2("Na farme mame od roku 2012 12 kráv a 230 oviec.")
uloha2("Skutok sa stal.")
uloha2("snehulienka a 7 trpazlikov.")
