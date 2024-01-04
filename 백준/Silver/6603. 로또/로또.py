import itertools
import sys
while True:
    l = list(map(int,input().split()))
    if l[0]==0:
        break
    del l[0]

    lotto = itertools.combinations(l,6)
    for i in lotto:
        print(*i)
    print()