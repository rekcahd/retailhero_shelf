import sys
import numpy as np
line = sys.stdin.readline()
n,k,m,h,w,D0 = map(int,line.split(" "))
#категория, бренд и базовая прибыльность продукта соответственно
goods = np.zeros((n,3),dtype=int)
byt = list(list() for i in range(k))
for i in range(n):
    goods[i] = list(map(int,sys.stdin.readline().split(" ")))
    byt[goods[i][0]-1].append(i)
ans = np.zeros([h,w],dtype=int)
rs = np.zeros([h],dtype=int)
for cat in sorted(byt,key=lambda x:-len(x)):
    free_place = (-rs-len(cat)+w)    
    if free_place[free_place >= 0].shape[0] > 0:
        j = (free_place==free_place[free_place >= 0].min()).argmax()
    else:
        j = rs.argmin()
    if rs[j] >= w:continue
    ans[j,rs[j]:rs[j]+len(cat)] = np.array(cat)[:(w-rs[j])]+1
    rs[j]+=len(cat)
sys.stdout.write("\n".join(" ".join(map(str,row)) for row in ans)+"\n")