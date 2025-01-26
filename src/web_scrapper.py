"""
Class Web Scrapper.
"""

from abc import abstractmethod

from singleton import Singleton


class WebScrapper(Singleton):
    """
    Classe base para implementação de um Web Scrapper.

    Esta classe é um Singleton, garantindo que apenas uma instância do Web Scrapper
    seja criada durante a execução do programa. Ela define métodos abstratos que devem
    ser implementados por classes derivadas para configurar, captar e persistir dados.

    Métodos:
        config(): Configura o Web Scrapper.
        captar(): Captura dados de uma fonte específica.
        persistir(): Persiste os dados capturados.
        scrapping(): Executa o processo completo de captura e persistência.
    """

    @abstractmethod
    def config(self) -> None:
        """
        Método abstrato para configurar o Web Scrapper.

        Este método deve ser implementado por classes derivadas para configurar
        quaisquer parâmetros necessários para o funcionamento do scrapper.
        """
        raise NotImplementedError

    @abstractmethod
    def captar(self) -> None:
        """
        Método abstrato para captar dados.

        Este método deve ser implementado por classes derivadas para realizar a
        captura de dados de uma fonte específica, como uma página web ou API.
        """
        raise NotImplementedError

    @abstractmethod
    def persistir(self) -> None:
        """
        Método abstrato para persistir dados.

        Este método deve ser implementado por classes derivadas para salvar ou
        processar os dados capturados, como armazená-los em um banco de dados ou
        arquivo.
        """
        raise NotImplementedError

    def scrapping(self) -> None:
        """
        Executa o processo completo de captura e persistência de dados.

        Este método chama os métodos `captar` e `persistir` em sequência, realizando
        o fluxo completo de um web scraping.
        """
        self.captar()
        self.persistir()
