import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def dict_to_csv(filename, disciplines):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nome', 'Codigo'])
        for discipline in disciplines:
                writer.writerow([discipline['Nome'], discipline['Codigo']])


def scrape():
    # url da pagina do curriculo de eng. de software
    url = "https://matriculaweb.unb.br/graduacao/curriculo.aspx?cod=6360"

    # abrindo conexao e puxando o html da pagina
    uReq = urlopen(url)
    html = uReq.read()
    uReq.close()

    # convertendo html
    page_soup = soup(html, "html.parser")
    table_list = page_soup.findAll("table", {"id": "datatable"})


    table_list.remove((table_list[0]))


    discipline_code_list = []
    discipline_names = []

    #extraindo do html os codigos das disciplinas
    for i in range(len(table_list)):
        for table_row in table_list:
            td = table_row.find("td").text
            discipline_code_list.append(td)

    #extraindo do html os nomes das disciplinas
    for i in range(len(table_list)):
        for discipline in table_list:
            discipline_name = discipline.find("a").text
            discipline_names.append(" ".join(discipline_name.split()))

    disciplines = []
    for i in range(len(discipline_names)):
        temp = {}
        temp['Nome'] = discipline_names[i]
        temp['Codigo'] = discipline_code_list[i]
        disciplines.append(temp)


    dict_to_csv('disciplines.csv', disciplines)
    return pd.read_csv("disciplines.csv")
