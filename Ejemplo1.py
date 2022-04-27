import xlrd
import pandas as pd
import numpy as np
data=pd.read_excel('BI_Clientes.xlsx')
rango=np.arange(-1,6,1)
frec=pd.cut(data['TotalChildren'],rango)
tabla=pd.value_counts(frec)

print(tabla)