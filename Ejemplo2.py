import math

import xlrd
import pandas as pd
import numpy as np
data=pd.read_excel('BI_Alumnos.xlsx')
min=pd.DataFrame(data).min()
max=pd.DataFrame(data).max()
r=max-min
n=pd.DataFrame(data).count()
k=1+3.3*math.log10(n)
tic=r/k
##print(min,'',max,'',n,'',k,'',tic)
rango=np.arange(9.0,15.3,0.9)
frecuencia=pd.cut(data['Nota'],rango)
tabla=pd.value_counts(frecuencia)
print('Tabla de frecuencia')
print(tabla)


