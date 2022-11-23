import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'html.parser')

StarTable = soup.find_all('table')
StarNames = []
Distance =[]
Mass = []
Radius =[]
temp_list= []

table_rows = StarTable[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    
    StarNames.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(StarNames,Distance,Mass,Radius,)),columns=['StarName','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_star.csv')