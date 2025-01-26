"""
Uma classe para coletar artigos recentes da categoria de IA em Ciência da Computação do arXiv.
Herda da classe WebScrapper para definir o comportamento de coleta e o tratamento de dados.
Salva os dados coletados em um arquivo CSV.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dataclass import Ai_Authors, Ai_Links, Ai_Title
from logger import Logger
from web_scrapper import WebScrapper

logger = Logger().get_logger()


class arxiv_scrapper(WebScrapper):
    """
    A class to scrape recent articles from the arXiv Computer Science AI category.
    Inherits from the WebScrapper class to define scraping behavior and data handling.
    """

    def config(self) -> None:
        """
        Configure the base URL for the arXiv Computer Science AI category page and
        retrieves the page content using the requests library.
        It parses the HTML content with BeautifulSoup for further scraping.
        """
        url_base = 'https://arxiv.org/list/cs.AI/recent'
        page = requests.get(url_base)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def pegar_arquivos(self) -> None:
        """
        Extract the section of the webpage that contains the articles.
        The articles are contained in the 'articles' HTML element, which is found
        by its id attribute.
        """
        self.arquivos = self.soup.find(id='articles')

    def captar_dados(self) -> None:
        """
        Extract the titles, authors, and PDF links of the articles from the webpage.
        It processes the raw HTML to gather clean data that can be structured into a DataFrame.
        """
        # Extract article titles
        title = self.arquivos.find_all('div', class_='list-title mathjax')
        titles_list = []
        for item in title:
            clean_title = (
                item.text.replace('Title:\n          ', '')
                .replace('\n        ', '')
                .strip()
            )
            titles_list.append(Ai_Title(title=clean_title))

        # Extract authors
        list = self.arquivos.find_all('div', class_='list-authors')
        list_authors = []
        for item in list:
            authors = []
            for element in item:
                if element.text != ', ':
                    authors.append(Ai_Authors(author=element.text))
            list_authors.append(authors)

        # Extract PDF links
        links = self.soup.find_all('a', string='pdf')
        links_list = []
        for element in links:
            links_list.append(Ai_Links(link='https://arxiv.org/' + element['href']))

        # Create a DataFrame
        self.df = pd.DataFrame(
            {'Title': titles_list, 'Authors': list_authors, 'Link': links_list}
        )

    def persistir(self) -> None:
        """
        Save the scraped data into a CSV file ('dados_artigos_ai.csv').
        If an error occurs during the file writing, it logs the error message.
        """
        try:
            self.df.to_csv('dados_artigos_ai.csv', index=False)

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise


if __name__ == '__main__':
    # Instantiate the scrapper and run the scraping process
    arxiv_scrapper = arxiv_scrapper()
    arxiv_scrapper.config()
    arxiv_scrapper.pegar_arquivos()
    arxiv_scrapper.captar_dados()
    arxiv_scrapper.persistir()
