#!/bin/python3

import sys

s = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
     "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr",
     "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la",
     "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w ", "re", "os",
     "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am",
     "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl",
     "mc", "lv", "ts", "og"]

readable = []
if len(sys.argv) < 2:
    print('No Input! Please provide an element symbol or Z number as command line argument.')
    quit(1)
for i in sys.argv[1:]:
    if i.lower() in s or 0 < int(i) <= 118:
        readable.append(i)
unreadable = [x for x in sys.argv[1:] if x not in readable]
if len(unreadable) > 0:
    print(f"Can't convert argument(s):", *unreadable)

output = []
for z in readable:
    if z.lower() in s:
        z_number = s.index(z.lower()) + 1
        output.append(z_number)
    elif str.isdigit(z):
        elem_symbol = s[int(z)-1].capitalize()
        output.append(elem_symbol)

if len(output) > 0:
    print(f"Output:", *output)
