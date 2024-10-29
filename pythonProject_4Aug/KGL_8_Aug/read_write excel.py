import pandas as pd
from pandas import read_excel

#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape :- use r in front of absolute path
#Use a raw string by adding an r before the string, which tells Python to ignore special characters in the string:

xls = r"C:\Users\nagur\Downloads\Preparation.xlsx"

# xls = "C:/Users/nagur/Downloads/Preparation.xlsx"
# xls = "C:\\Users\\nagur\\Downloads\\Preparation.xlsx"

df=read_excel(xls)
print(df)

#installed pandas library first :- pip install pandas
#install openpyxl to read n write xls :- pip install openpyxl
#by default it will read 1st sheet in xls