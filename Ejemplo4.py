import xlrd
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx')

#Describe
grupo1=data.groupby('SpanishEducation')
print(grupo1.describe())

#Conteo
grupo2=data.groupby('SpanishEducation').count()
print(grupo2)

grupo3=data.groupby('SpanishEducation')['SpanishEducation'].count()
print(grupo3)

#Sumando el sueldo agrupando al nivel educativo en español
grupo4=data.groupby('SpanishEducation')['YearlyIncome'].sum()
print(grupo4)

#el sueldo promedio agrupando al nivel educativo en español
grupo5=data.groupby('SpanishEducation')['YearlyIncome'].mean()
print(grupo5)

grupo3.plot(kind='bar')
plt.show()


grupo4.plot(kind='pie')
plt.show()


grupo5.plot(kind='barh')
plt.show()