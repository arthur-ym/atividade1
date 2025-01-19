from bs4 import BeautifulSoup
from dataclass import RawCursos, RawProfessores
from logger import Logger
from requests import get
from utils import get_df_from_model_list
from web_scrapper import WebScrapper, WebScrapperFactory

# --------------------------
# -------DESC: Logger-------
logger = Logger().get_logger()
# --------------------------


# ConcreteProduct
class ItiScrapperCursos(WebScrapper):
    def config(self):
        url_base = 'https://iti.ufscar.mba/'

        response = get(url_base)

        response.encoding = 'UTF-8'

        self.soup = BeautifulSoup(response.text, 'html.parser')

    def captar(self) -> None:
        try:
            # -----Nossos cursos -----

            nossos_cursos = self.soup.find(id='nossos-cursos')

            container_default = nossos_cursos.find(class_='container-default')

            vector_models = []
            cursos_disponiveis = container_default.find_all(class_='box-curso')
            for i in cursos_disponiveis:
                if 'ocultar' not in i['class']:
                    vector_models.append(
                        RawCursos(curso=i.find(class_='h2-nome-do-curso').text)
                    )

            self.df = get_df_from_model_list(models=vector_models)

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise

    def persistir(self) -> None:
        try:
            self.df.to_csv('dados_iti_cursos.csv')

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise


# ConcreteProduct
class ItiScrapperProfessores(WebScrapper):
    def config(self):
        url_base = 'https://iti.ufscar.mba/'

        response = get(url_base)

        response.encoding = 'UTF-8'

        self.soup = BeautifulSoup(response.text, 'html.parser')

    def captar(self) -> None:
        try:
            nosso_time = self.soup.find(id='nosso-time')

            coluna_docentes = nosso_time.find(class_='fundo-coluna-docentes')

            # -----Professores da Academia-----

            professores_academia = coluna_docentes.find_all(class_='card-profs-home')

            vector_models = []

            for i in professores_academia:
                vector_models.append(
                    RawProfessores(
                        nome=i.find(class_='h4-nome-professor').text,
                        instituicao=i.find(class_='h5-org-prof').text,
                        tipo='academia',
                    )
                )

            # -----Professores do Mercado de Trabalho-----

            coluna_representantes = nosso_time.find(
                class_='fundo-coluna-representantes'
            )

            professores_industria = coluna_representantes.find_all(
                class_='card-profs-home'
            )

            for i in professores_industria:
                vector_models.append(
                    RawProfessores(
                        nome=i.find(class_='h4-nome-professor').text,
                        instituicao=i.find(class_='h5-org-prof').text,
                        tipo='mercado',
                    )
                )

            self.df = get_df_from_model_list(models=vector_models)

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise

    def persistir(self) -> None:
        try:
            self.df.to_csv('dados_iti_professores.csv')

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise


# ConcreteCreator
class ItiScrapperFactory(WebScrapperFactory):
    def createScrapper(self, *, tipo: str) -> WebScrapper:
        if tipo == 'cursos':
            return ItiScrapperCursos()
        elif tipo == 'professores':
            return ItiScrapperProfessores()
        else:
            raise ValueError


if __name__ == '__main__':
    iti_scrapper_factory = ItiScrapperFactory()

    iti_scrapper_cursos = iti_scrapper_factory.createScrapper(tipo='cursos')
    iti_scrapper_cursos.config()
    iti_scrapper_cursos.scrapping()

    iti_scrapper_professores = iti_scrapper_factory.createScrapper(tipo='professores')
    iti_scrapper_professores.config()
    iti_scrapper_professores.scrapping()
