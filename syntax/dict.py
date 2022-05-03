from collections import OrderedDict
 
# >= python 3.7 dict's insertion is ordered by default, no need to use OrderedDict
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

