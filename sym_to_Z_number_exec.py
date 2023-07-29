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
    for d in range(len(arg)):
        if isinstance(arg[d], str):
            arg[d] = arg[d].strip()
    readable = []
    if len(arg) == 0:
        print('No Input! Please provide an element symbol or Z number as command line argument.')
        quit(1)
    arg = list(map(lambda x: x.lower() if str(x).isalpha() else x, arg))
    for i in arg:
        if str(i).lower() in s or str(i).lstrip('-').isdigit():
            readable.append(i)
    unreadable = [x for x in arg if x not in readable]
    if len(unreadable) > 0:
        print(f"Can't convert argument(s):", *unreadable)
        quit(1)
    list1 = []
    too_big = []
    too_small = []
    for k in readable:
        if isinstance(k, int) and k > len(s):
            too_big.append(k)
            continue
        if str.isdigit(str(k).lstrip('-')) and int(k) <= 0:
            too_small.append(k)
            continue
        if k in s:
            list1.append(s.index(k) + 1)
        elif str.isdigit(str(k)):
            list1.append(s[int(k) - 1].capitalize())
    if len(too_big) > 0 or len(too_small):
        too_big = ', '.join(map(str, too_big))
        too_small = ', '.join(map(str, too_small))
        if len(too_big) > 0:
            print(f"Atomic/Z number ({too_big}) is brobdingnagian, doesn't exist")
        if len(too_small) > 0:
            print(f"Atomic/Z numbers ({too_small}) are 0 or negative, doesn't exist!")
        quit(1)
    print(*list1)
