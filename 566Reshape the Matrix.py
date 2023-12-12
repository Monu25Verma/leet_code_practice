import numpy as np
import pandas as pd

mat = [[1, 2],[3, 4]]
r = 1
c= 4
flatt = []
new_mat = []
for i in mat:
    for row in i:
        flatt.append(row)
if len(flatt) != r * c:
    print(mat)
else:
    for j in range(r):
        new_mat.append(flatt[j * c: j * c + c])
print(new_mat)

