import requests
from bs4 import BeautifulSoup


url = "https://www.scoresheets.cc/thomazpp"
#https://www.scoresheets.cc/henriqueboaventura
#https://www.scoresheets.cc/giraia

# Envie uma solicitação GET para a página
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analise o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre o preço do produto - ajuste o seletor conforme necessário
