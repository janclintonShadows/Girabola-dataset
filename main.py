from webScrap_Girabola import BeSoccerScoreBoardScrap as bssb
import pandas as pd

if __name__ == '__main__':
    url = 'https://pt.besoccer.com/competicao/tabela/girabola/'
    girabola = bssb(url=url,date_range=(2006,2023))
    # Vamos passar esses dados para um dataframe, fazer umas pequenas limpezas e salvar como csv
    df = pd.DataFrame(girabola.compute_scraping())
    # removendo alguns erros em certos dados
    df['PJ'] = df.PJ.str.replace('\\n-\d+','')
    # mudando o nome das equipas para estarem com as iniciais maiúsculas e o resto minuscula
    df['TIME'] = df['TIME'].str.title()
    # retificando os dados do time petro, já que aparece com dois nomes diferentes
    df['TIME'] = df['TIME'].str.replace('Petro Atletico','Petro De Luanda')
    # Froçar todas as colunas com dados numericos para o tipo numerico
    colunas = ['POS', 'PTS', 'PJ', 'JG', 'E', 'D', 'GP', 'GC', 'SG', 'ANO']
    for col in colunas:
        df[col] = pd.to_numeric(df[col],errors='coerce')
    # Aqui vamos salvar os dados em formato csv em uma pasta
    df.to_csv('dataset/tabela_girabola.csv',index=False)