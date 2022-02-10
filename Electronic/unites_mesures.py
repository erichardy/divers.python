
from pdb import set_trace as st

s = {}
s['cent'] = 100
s['dix'] = 10
s['un'] = 1

d = {}
d['milli'] = .001
d['micro'] = .000001
d['nano'] =  .000000001
d['pico'] =  .000000000001

# print("\t", "\t", "0.123456789012", "\t")

for xd in d:
    if xd == 'milli':
        print("\t", "\t", "0.123", "\t")
    if xd == 'micro':
        print("\t", "\t", "0.123456", "\t")
    if xd == 'nano':
        print("\t", "\t", "0.123456789", "\t")
    if xd == 'pico':
        print("\t", "\t", "0.123456789012", "\t")
    for xs in s:
        val = s[xs] * d[xd]
        if xd == 'milli':
            fval = f"{val:.3f}\t\t"
        if xd == 'micro':
            fval = f"{val:.6f}\t"
        if xd == 'nano':
            fval = f"{val:.9f}\t"
        if xd == 'pico':
            fval = f"{val:.12f}\t"
        print(xs, '\t', xd, '\t', fval, f"{val:.0e}")
    print('----------------------------------------')

# st()
