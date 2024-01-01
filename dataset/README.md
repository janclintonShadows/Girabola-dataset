# Girabola WebScraping

Aqui vamos fazer o we Scrapping com Python, e usando um pouco de IA Generativa do Google Colab para ajudar no processo de webscrapping.

Este projecto consiste em fazer o WebScraping dos dados do site BeSoccer para obter dados das tabelas de resultados de campeonatos.
Para o nosso projecto pegaremos os dados do Girabola, campeonato Angola de Futebol, entre os anos 2006 ate 2023, sendo que para os anos anteriores as 2006 o site parece não possuir essas informações.

Os dados pegos serão os já conhecidos nas tabelas de resultados de futebol:

- POS: Classificaçao do time no campeonato naquele ano
- TIME: O nome do time
- PTS: Pontos, que são a soma dos pontos ganhos por vitórias e empates.
- PJ: Partidas jogadas, que são o número de jogos disputados pela equipe.
- JG: Jogos ganhos, que são o número de vitórias da equipe.
- E: Empates, que são o número de jogos em que a equipe não perdeu nem ganhou.
- D: Derrotas, que são o número de jogos em que a equipe perdeu.
- GP: Gols pró, que são o número de gols marcados pela equipe.
- GC: Gols contra, que são o número de gols sofridos pela equipe.
- SG: Saldo de gols, que é a diferença entre gols pró e gols contra.

Para fazer o Web Scraping fizemos o uso de dois pacotes essenciais, o requests e o BeautifulSoup, também faremos uso do pandas para retificar alguns pontos do nosso dataset, e depois salvar-lo em cvs.

