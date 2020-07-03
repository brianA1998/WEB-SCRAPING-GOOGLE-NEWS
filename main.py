import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrRlNLQUFQAQ?hl=es-419&gl=AR&ceid=AR%3Aes-419'


if __name__ == '__main__':

    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        #news_dia_mes_año.txt
        now = datetime.now().strftime('%d_%m_%Y')
        file_path = f'WEB-SCRAPPER-GOOGLE-NEWS/news_{now}.txt'

        with open('file_path','w+') as file:

            for h3 in soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb', limit=20):
                title = h3.a.text
                
                file.write(title + '\n')