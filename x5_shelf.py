import sys
import numpy as np
import pandas as pd
line = sys.stdin.readline()
# n продуктов, k категорий, m брендов, h рядов, w позиций, D0 коэффициент бонуса за разнообразие категорий
n,k,m,h,w,D0 = map(int,line.split(" "))
#категория, бренд и базовая прибыльность продукта соответственно
goods = pd.DataFrame(
                    np.array(list(list(map(int,sys.stdin.readline().split(" "))) for i in range(n)),dtype=int),
                    columns = ["cat","brand","profit"]
                    )
goods = goods.sort_values("profit",ascending = False).head(h*w)
byt = list(data['index'].values for gr_id,data in goods.reset_index().sort_values("profit",ascending = False).groupby(["cat"]))
ans = np.zeros([h,w],dtype=int)
rs = np.zeros([h],dtype=int)
for cat in sorted(byt,key=lambda x:-len(x)):
    free_place = (-rs-len(cat)+w)
    if free_place[free_place >= 0].shape[0] > 0:
        j = (free_place==free_place[free_place >= 0].min()).argmax()
        cat = goods.loc[cat].sort_values("brand").index
    else:
        j = rs.argmin()
    if rs[j] >= w:continue
    ans[j,rs[j]:rs[j]+len(cat)] = np.array(cat)[:(w-rs[j])]+1
    rs[j]+=len(cat)
sys.stdout.write("\n".join(" ".join(map(str,row)) for row in ans)+"\n")