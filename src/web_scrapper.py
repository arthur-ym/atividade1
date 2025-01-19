from abc import abstractmethod

from singleton import Singleton


# Product
class WebScrapper(Singleton):
    @abstractmethod
    def config(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def captar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def persistir(self) -> None:
        raise NotImplementedError

    def scrapping(self) -> None:
        self.captar()
        self.persistir()


# Creator
class WebScrapperFactory(Singleton):
    @abstractmethod
    def createScrapper(self) -> WebScrapper:
        raise NotImplementedError
