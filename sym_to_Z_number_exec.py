#!/bin/python3

s = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
     "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr",
     "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la",
     "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w ", "re", "os",
     "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am",
     "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl",
     "mc", "lv", "ts", "og"]


def convert(*arg):
    arg = list(arg)
    readable = []
    if len(arg) == 0:
        print('No Input! Please provide an element symbol or Z number as command line argument.')
        quit()
    arg = map(lambda x: x.lower() if str(x).isalpha() else x, arg)
    for i in arg:
        if str(i).lower() in s or str.isdigit(str(i)):
            readable.append(i)
    unreadable = [x for x in arg if x not in readable]
    if len(unreadable) > 0:
        print(f"Can't convert argument(s):", *unreadable)
        quit()
    list1 = []
    too_big = []
    for k in readable:
        if isinstance(k, int) and k > len(s):
            too_big.append(k)
            continue
        if k in s:
            list1.append(s.index(k) + 1)
        elif str.isdigit(str(k)):
            list1.append(s[k - 1].capitalize())
    if len(too_big) > 0:
        too_big = ', '.join(map(str, too_big))
        print(f"Atomic/Z number ({too_big}) is brobdingnagian, doesn't exist")
        quit()
    print(*list1)


convert(1, 2, 3, 'h', 'mg')

