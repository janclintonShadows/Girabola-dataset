"""
Este projecto consiste em fazer o WebScraping dos dados do site BeSoccer para obter dados das tabelas de resultados de campeonatos.
Para o nosso projecto pegaremos os dados do Girabola, campeonato Angola de Futebol, entre os anos 2006 ate 2023, sendo que para os anos anteriores as 2006 o site parece não possuir essas informações.

Os dados pegos serão os já conhecidos nas tabelas de resultados de futebol:

POS - Classificaçao do time no campeonato naquele ano
TIME - O nome do time
PTS: Pontos, que são a soma dos pontos ganhos por vitórias e empates.
PJ: Partidas jogadas, que são o número de jogos disputados pela equipe.
JG: Jogos ganhos, que são o número de vitórias da equipe.
E: Empates, que são o número de jogos em que a equipe não perdeu nem ganhou.
D: Derrotas, que são o número de jogos em que a equipe perdeu.
GP: Gols pró, que são o número de gols marcados pela equipe.
GC: Gols contra, que são o número de gols sofridos pela equipe.
SG: Saldo de gols, que é a diferença entre gols pró e gols contra.

Para fazer o Web Scraping fizemos o uso de dois pacotes essenciais, o requests e o BeautifulSoup, também faremos uso do pandas para retificar alguns pontos do nosso dataset, e depois salvar-lo em cvs.

"""

# importando os modulos que iremos usar
import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs
# vamos importar o modulo de data
from datetime import date as dt

# Vamos criar uma classe para podermos pegar os dados
class BeSoccerScoreBoardScrap:
    def __init__(self,url:str,date_range:tuple or list) -> None:
        """
        Essa função recebe dados de uma url do site BeSoccer, e procura o placar de classificação do campeonato dentro de um intervalo de datas.
        :param url: a url da fonte dos dados, como uma string
        :param date_range: uma tupla com a ano de início e a ano de final dos dados que pretende obter
        :return: um objeto com os dados obtidos, ou None se houver algum erro
        """
        self.__data = {
            'POS':[],
            'TIME':[],
            'PTS':[],
            'PJ':[],
            'JG':[],
            'E':[],
            'D':[],
            'GP':[],
            'GC':[],
            'SG':[],
            'ANO':[]
                }
        self.__url = url
        self.__init_date:int = int(date_range[0])
        self.__final_date:int = int(dt.today().year)
        if len(date_range)==1:
            self.__init_date = date_range[0]
        elif len(date_range)==2:
            self.__init_date = date_range[0]
            self.__final_date = date_range[1]
        else:
            raise('The date_range value must be a tuple of 2 elements of Integer type representing the season date')
        
    def compute_scraping(self):
        """
        Essa função computa o web scraping da pagina do Bessocer, e retorna um sicionario de todos os dados
        :return: dict, um objecto do tipo dicionario ou None se houver algum erro
        """
        for i in range(self.__init_date,self.__final_date+1):
            
            link = self.__url + str(i)
            html = req.get(link).text
            page = bs(html,'html.parser')
            ano = page.find('h1',class_='mr10').get_text().split(' ')[-1]
            for linha in page.find('div',class_='table-body table-custom competition-result').find_all('tr',class_='row-body'):
                pos = linha.find('td',class_='number-box').get_text().strip()
                nome = linha.find('span',class_='team-name').get_text().strip()
                pts = linha.find('td',class_='green bold br-l').get_text().strip()
                siglas = linha.find_all('td')[-7:]
                # Partidas jogadas, que são o número de jogos disputados pela equipe.
                PJ = siglas[0].get_text().strip() 
                # Jogos ganhos, que são o número de vitórias da equipe.
                JG = siglas[1].get_text().strip() 
                # Empates, que são o número de jogos em que a equipe não perdeu nem ganhou
                E = siglas[2].get_text().strip() 
                # Derrotas, que são o número de jogos em que a equipe perdeu.
                D = siglas[3].get_text().strip() 
                # Gols pró, que são o número de gols marcados pela equipe.
                GP = siglas[4].get_text().strip() 
                # Gols contra, que são o número de gols sofridos pela equipe.
                GC = siglas[5].get_text().strip() 
                # Saldo de gols, que é a diferença entre gols pró e gols contra.
                SG = siglas[6].get_text().strip()

                # adiconando tudo em um dicionario 
                self.__data['POS'].append(pos)
                self.__data['TIME'].append(nome)
                self.__data['PTS'].append(pts)
                self.__data['PJ'].append(PJ)
                self.__data['JG'].append(JG)
                self.__data['E'].append(E)
                self.__data['D'].append(D)
                self.__data['GP'].append(GP)
                self.__data['GC'].append(GC)
                self.__data['SG'].append(SG)
                self.__data['ANO'].append(ano)

        return self.__data
