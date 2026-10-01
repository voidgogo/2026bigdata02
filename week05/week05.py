import seaborn as sns
import pandas as pd

df1 = sns.load_dataset("penguins")
#print(df1.head())
#print(df1.describe())
#print(df1.query('bill_length_mm < 35'))
#print(df1[df1['bill_length_mm'] < 35])
#print(df1.loc[df1['bill_length_mm'] < 35])
#print(df1.query('bill_length_mm > 54 and species == "Chinstrap"'))

# blmm= float(input("부리 길이 입력 : "))
# spcs = input("펭귄 종류(Gentoo/Chinstrap/Adelie) 입력 : ")
# print(df1.query('bill_length_mm > @blmm and species == @spcs'))

# print(df1.query('island.str.contains("sc")'))
print(df1.query('species.str.startswith("C")'))

penguins = ["Gentoo", "Chinstrap"]
print(df1.query('species.isin(@penguins)'))