import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# url da pagina do curriculo de eng. de software
url = "https://matriculaweb.unb.br/graduacao/curriculo.aspx?cod=6360"

# abrindo conexao e puxando o html da pagina
uReq = urlopen(url)
html = uReq.read()
uReq.close()

# convertendo html
page_soup = soup(html, "html.parser")
table_list = page_soup.findAll("table", {"id": "datatable"})


print(len(table_list))
table_list.remove((table_list[0]))

row_list = []
discipline_code_list = []
discipline_names = []
for i in range(len(table_list)):
    for table_row in table_list:
        tr = table_row.find("tr")
        row_list.append(tr)


for i in range(len(row_list)):
    for discipline in table_list:
        discipline_name = discipline.find("a")
        discipline_names.append(discipline_name)






print("Table List " + str(len(table_list)) + str(table_list))
print("\n")
print("Row List " + str(len(row_list)) + str(row_list) )
print("\n")
print("Discipline name list " + str(len(discipline_names)) + str(discipline_names))


