#!/bin/python3

#############################################
#Author: Kai Weterings
#Date: 30/07/2023

#https://github.com/kweterings/Sym_To_Z_Number
#############################################

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
    arg = list(map(lambda x: x.lower() if x.isalpha() else x, arg))
    for i in arg:
        if i.lower() in s or str.isdigit(i.lstrip('-')):
            readable.append(i)
    unreadable = [x for x in arg if x not in readable]
    if len(unreadable) > 0:
        print(f"Can't convert argument(s):", *unreadable)
    list1 = []
    too_big = []
    too_small = []
    for k in readable:
        if str.isdigit(k) and int(k) > len(s):
            too_big.append(k)
            continue
        if str.isdigit(k.lstrip('-')) and int(k) <= 0:
            too_small.append(k)
            continue
        if k in s:
            list1.append(s.index(k) + 1)
        elif str.isdigit(str(k)):
            list1.append(s[int(k) - 1].capitalize())
    if len(too_big) > 0:
        too_big = ', '.join(map(str, too_big))
        print(f"Atomic/Z number ({too_big}) is brobdingnagian, doesn't exist!")
    if len(too_small) > 0:
        too_small = ', '.join(map(str, too_small))
        print(f"Atomic/Z numbers ({too_small}) are 0 or negative, doesn't exist!")
    print(*list1)


cond = True
n = 1
while cond:
    if n == 1:
        user_input = input("What Element Symbol or Atomic/Z number would you like to convert? You may enter as many "
                           "as you'd like (No commas!). (to quit, type q):")
        n = 0
    else:
        user_input = input("What Element Symbol or Atomic/Z number would you like to convert? (to quit, type q):")
    if 'q' in user_input.lower().replace(" ", ""):
        quit()
    convert(*user_input.split())
